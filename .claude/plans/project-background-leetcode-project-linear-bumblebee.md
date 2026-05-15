# LeetCode Repo Refactor — Phase 1: TUI (Go + Bubble Tea) + Socratic Tutor

## Context

這個 repo 是從研究所時期維護至今的 LeetCode 練習庫,~600+ 題,每題的 scaffolding(建資料夾、貼題目、寫測試、更新 README、提交、記錄失敗 case、補 Note)目前**全靠手動**,摩擦大到讓「每日一題」與「Weekly Contest」逐漸停滯。

主要不爽點:
1. **Daily / Weekly 摩擦**:從 LeetCode 抓題目到 repo、寫完提交看結果、把失敗 case 記下來,目前要手動切瀏覽器+貼 markdown+貼 starter code,很容易懶得弄。
2. **README 是純 markdown 表格**(600+ 行),手動維護易出錯。
3. **CI 還在 Travis**(Python 3.9 only,無 lint),tooling 落後。
4. **被別人解法啟發或練多解時**只能自己寫 Note,沒有「老師式引導」工具幫忙真正內化。

本次目標(已與用戶確認):**把 daily + weekly 摩擦降到一條指令、加一個 Socratic Tutor agent skill 用於引導式解題**。

關鍵決策:
- **TUI 用 Go + Bubble Tea**(非 Python):核心訴求是流暢度與 startup 體感。Go 給 single binary、<50ms startup、Charm 生態(Bubble Tea/Lipgloss/Bubbles/Glamour/Huh)動畫順、跨平台分發乾淨。Repo 主語言 Python 不變,工具語言獨立。
- **Repo 結構不破壞**:現有資料夾命名、README 格式、test 慣例全部沿用。
- **資料結構化、Contest 重組、CI 遷移、mkdocs、舊題現代化**全進 backlog。

---

## Current State 摘要(已 verify)

| 項目 | 現況 | 後續處理 |
|---|---|---|
| 專案根 | 無 `pyproject.toml`,只 `requirements.txt`(pytest/cov/numpy 4 行) | Phase 1 在 `tools/leet/` 開新 Go module,不動主 repo |
| README | 純 markdown 表格,~600 列,人工維護(`👍`/`*`/`▲` 標註) | Phase 1 不動;TUI 印出建議 row 給用戶手貼 |
| Daily 題 | 散落 `Python3/{Category}/{ProblemName}/`,`Strategy[ID].py` + `test_[ID].py` 慣例 | TUI 自動推導 category(由 LeetCode tags 對應現有 12 類資料夾) |
| Weekly Contest | `Contest/LeetCodeWeeklyContest/WeeklyContest{N}/{1,2,3,4}/`,**沒測試也沒 README** | TUI scaffold 4 題(問題 md + Solution.py + 可選 test_.py),結構不動 |
| 測試慣例 | 模組頂層 `testcases = [(input, expected), ...]` + `def test_X(): for ... assert`(見 `Python3/Array/MatrixDiagonalSum/test_1572.py:4-18`) | 沿用;TUI 把 LeetCode sample 預填進去(用 Go template 產生 .py) |
| 失敗 case | 目前散在 inline 註解 + 大型 case `.txt`(見 `Python3/Array/WordSearchII/large_case.txt`) | TUI submit 失敗時把 input 寫入 `cases/failed_YYYYMMDD.txt`(避免動既有 test 結構),並印一行「請手動 append 到 testcases」 |
| CI | `.travis.yml`(Py 3.9, pytest+codecov) | **Backlog**:遷 GH Actions + ruff + pre-commit |
| mkdocs | `.claude/skills/mkdocs-site-bootstrap` 已 symlink 但未啟用 | **Backlog** |
| `.claude/` | 已有 `settings.json`(只設 `plansDirectory`)、`plans/`、skills symlink | Phase 1 加 socratic-tutor skill |

---

## Phase 1 Scope

### A. `tools/leet/` — Go module(Bubble Tea TUI + Cobra CLI)

**為什麼 Go**:
- **Startup**:Bubble Tea binary 冷啟動 <50ms(Python+Textual ~300-500ms)— 對「我想看一下今天 daily」這種高頻動作差別非常明顯。
- **流暢度**:Bubble Tea 是 Elm-style MVU,渲染走 diff,少量 alloc;高 refresh rate 下 Lipgloss 渲染穩定。
- **分發**:`go install` 或 `go build` 給 single binary,跨平台無 runtime 依賴。Repo 之外的同事/未來自己換機器都能秒裝。
- **生態**:Charm 套件齊(Bubbles 內建 list/textarea/spinner/viewport/help,Glamour 渲染 markdown,Huh 處理表單),不用自己造輪子。

**結構**:
```
tools/leet/
├── go.mod                          # module github.com/daviddwlee84/LeetCode/tools/leet
├── go.sum
├── Makefile                        # build/install/test/lint
├── README.md                       # 用法 + auth 設定步驟
├── cmd/
│   └── leet/
│       └── main.go                 # cobra root,組裝子命令
├── internal/
│   ├── cli/                        # cobra commands
│   │   ├── auth.go                 # leet auth
│   │   ├── daily.go                # leet daily
│   │   ├── contest.go              # leet contest weekly|biweekly
│   │   ├── submit.go               # leet submit
│   │   ├── test.go                 # leet test (wraps pytest)
│   │   ├── readme.go               # leet readme-row
│   │   └── tui.go                  # leet tui
│   ├── tui/                        # Bubble Tea models
│   │   ├── app.go                  # root model + screen routing
│   │   ├── list.go                 # 問題/比賽列表(bubbles/list)
│   │   ├── detail.go               # 題目內容(glamour 渲染 markdown)
│   │   ├── editor.go               # $EDITOR 啟動 + 還原 terminal
│   │   ├── result.go               # 提交結果面板(verdict + diff)
│   │   ├── scaffold_form.go        # 推導 category 的確認表單(huh)
│   │   └── styles.go               # lipgloss 樣式集中
│   ├── leetcode/
│   │   ├── api.go                  # GraphQL client(httpx 等價:net/http + json)
│   │   ├── queries.go              # GraphQL query 模板(daily/contest/problem/submit)
│   │   ├── types.go                # response struct
│   │   └── pollers.go              # submit 後 poll judge 結果
│   ├── auth/
│   │   ├── store.go                # 讀寫 ~/Library/Application Support/leet/auth.toml
│   │   └── browser.go              # 引導用戶從 chrome:// 取 cookie 的步驟說明
│   ├── scaffold/
│   │   ├── gen.go                  # 生資料夾與檔案
│   │   ├── templates.go            # Go embed 的 .py / .md 模板
│   │   └── pascalcase.go           # title → PascalCase 轉換
│   ├── categories/
│   │   └── map.go                  # LeetCode tag → 本 repo category 對應表
│   ├── readme/
│   │   └── row.go                  # 產生建議 markdown row(印 stdout,不寫檔)
│   └── editor/
│       └── launch.go               # exec.Command + tea.ExecProcess(Bubble Tea 內建處理 terminal 還原)
└── testdata/
    ├── daily_response.json         # 假 GraphQL response
    └── contest_response.json
```

**核心 deps**:
- `github.com/charmbracelet/bubbletea` — TUI runtime
- `github.com/charmbracelet/bubbles` — 現成 widgets(list/textinput/viewport/spinner/help)
- `github.com/charmbracelet/lipgloss` — 樣式
- `github.com/charmbracelet/glamour` — markdown 渲染題目
- `github.com/charmbracelet/huh` — 互動表單(category 確認、cookie 輸入)
- `github.com/spf13/cobra` — CLI 子命令
- `github.com/go-resty/resty/v2` — HTTP/GraphQL client(比 net/http 簡潔)
- `github.com/pelletier/go-toml/v2` — auth.toml 讀寫
- `github.com/zalando/go-keyring` — 可選,把 cookie 存到 OS keyring(macOS Keychain),avoid 純文字檔

**子命令(MVP)**:

| 命令 | 行為 |
|---|---|
| `leet auth` | 互動引導貼 cookie(Huh 表單),寫入 keyring 或 `auth.toml`;`--check` 用 `userStatus` query 驗證 |
| `leet daily [--no-edit]` | 抓今日 daily → 推導 category → scaffold 資料夾 → 開 `$EDITOR` |
| `leet contest weekly [N\|--latest]` | 抓 weekly contest N(或最新)→ 4 個子資料夾 + sample tests |
| `leet contest biweekly [N\|--latest]` | 同上,biweekly |
| `leet test [path]` | 在該題目錄跑 `pytest test_*.py`,失敗時印 diff(Glamour 渲染) |
| `leet submit [path] [--strategy Naive\|Better\|...]` | 上傳指定 .py 檔到 LeetCode,poll 結果,顯示 verdict;失敗把 input 寫入 `{folder}/cases/failed_YYYYMMDD.txt` |
| `leet tui` | Bubble Tea 互動模式,涵蓋以上所有(列表→選題→開編輯器→跑 test→submit→看結果) |
| `leet readme-row [path]` | 印出該題對應的 README 表格 row,讓用戶複製貼到正確位置 |

**Scaffolding 規則**(嚴格沿用現有慣例):
- 資料夾名:LeetCode title → PascalCase(`Power of Four` → `PowerOfFour`)
- Strategy 檔名:首次用 `Naive{ID}.py`(對齊 `Naive1572.py`、`Naive342.py`),後續解法用戶自取(`Better1572.py`、`Math342.py`、`Recursive342.py`)
- Test 檔名:`test_{ID}.py`,模組頂層 `testcases = [...]`,每個 strategy 一個 `def test_{Strategy}():`
- Note 檔名:`Note{ID}.md`(可選,`--with-note` flag)
- Daily 進 `Python3/{Category}/{ProblemName}/`;Contest 進 `Contest/LeetCodeWeeklyContest/WeeklyContest{N}/{idx}/`
- 模板用 Go `embed` package 內嵌,不靠外部檔案

**Category 對應表**(`internal/categories/map.go`):
LeetCode 常見 tag → 本 repo 12 類資料夾。優先級表(取第一個命中):
```go
var priority = []struct{ tag, dir string }{
    {"Linked List", "LinkedList"},
    {"Binary Tree", "BinaryTree"}, {"Tree", "BinaryTree"}, {"BST", "BinaryTree"},
    {"Graph", "Graph"}, {"DFS", "Graph"}, {"BFS", "Graph"},
    {"Dynamic Programming", "DynamicProgramming"},
    {"Bit Manipulation", "BitManipulation"},
    {"Binary Search", "Search"},
    {"Math", "Math"}, {"Number Theory", "Math"},
    {"Design", "Design"},
    {"Interactive", "Interactive"},
    {"String", "String"},
    {"Array", "Array"}, {"Hash Table", "Array"},  // HT 是次標籤
    // 預設 fallback: AdHoc(Greedy / Backtracking / Two Pointers / ...)
}
```
TUI 推導後若不確定(多個 tag 衝突),用 `huh.Select` 讓用戶確認,建議值預先 highlight。

**Auth flow**:
1. `leet auth` → Huh 表單顯示步驟:
   ```
   1. 開 Chrome → leetcode.com 已登入
   2. F12 → Application → Cookies → leetcode.com
   3. 複製 LEETCODE_SESSION 與 csrftoken
   ```
2. 兩個 textinput 收 cookie → 存 macOS Keychain(優先)或 `~/Library/Application Support/leet/auth.toml`(權限 0600)
3. 自動測試:`userStatus` GraphQL query 確認登入
4. 過期偵測:任何 401 → 自動提示重跑 `leet auth`

**Editor 整合**(`internal/editor/launch.go` + `internal/tui/editor.go`):
- 純 CLI 模式:`exec.Command(os.Getenv("EDITOR"), path).Run()`(Go 不需手動處理 SIGTSTP — runtime 已正確)
- TUI 內呼叫:用 `tea.ExecProcess(cmd, callback)` — Bubble Tea **官方支援**暫停 TUI、跑外部 process、自動還原 terminal 狀態(這是選 Bubble Tea 的關鍵理由之一,Python+Textual 要手動處理 stty)
- `$EDITOR` 預設 `nvim`,若未設則 fallback 到 `vi`

**Submit failed-case 邏輯**:
- LeetCode submit 回應若 `status_msg == "Wrong Answer"`,response 含 `last_testcase`、`expected_output`、`code_output`
- 寫入 `{problem_folder}/cases/failed_{YYYYMMDD}.txt`(內含 input + expected + got)
- 印一行提示:「✗ Wrong Answer。已存到 cases/failed_YYYYMMDD.txt — `leet test --merge-failed` 可幫你 append 進 test_{ID}.py」
- `--merge-failed`(進階):用 `pytest` 跑該 case 確認確實 fail,再 append 進 testcases list(暫時走 plain text append + 註解 marker `# leet:failed-case-start ... # leet:failed-case-end`,避免動到 ast)

### B. `.claude/skills/socratic-tutor/` — Agent Skill

**目的**:當用戶說「我卡在這題」「幫我想想」「`/socratic-tutor`」時,**不直接給答案**,而是像老師一樣引導。

**結構**(沿用 agentskills.io 規範,可用 `skill-author` skill 起手):
```
.claude/skills/socratic-tutor/
├── SKILL.md                         # 觸發描述 + 主流程
├── scripts/
│   └── analyze_complexity.py        # 可選:幫用戶寫的 code 估 time/space
└── reference/
    ├── greedy_proofs.md             # 常見 greedy 證明套路(交換論證、最優子結構)
    ├── dp_state_design.md           # DP 狀態設計檢核清單
    └── complexity_cheatsheet.md
```

**SKILL.md 主流程**:
1. **理解階段**:讀題目(用戶提供路徑或貼內容)→ 反問「你看到 input/output 後,腦中浮現的第一個想法是什麼?」
2. **方法分類**:不直接說答案,而是問「你覺得這題比較像 (a) 搜尋類 (b) 動態規劃 (c) 貪心 (d) 數學/觀察?為什麼?」
3. **漸進提示**(用戶卡住時):
   - L1:點出關鍵 observation(「注意 input 是已排序的」)
   - L2:指方向不指方法(「可以從兩端往中間想」)
   - L3:給出 sub-problem(「如果只有 2 個元素呢?3 個呢?」)
   - L4:才寫 pseudo-code
4. **證明階段**(greedy / 不變式):
   - 引用 `reference/greedy_proofs.md` 的交換論證模板,要求用戶套用
   - DP 題:要求列出 state、transition、base case、最終答案在哪
5. **複雜度分析**:用戶寫完後一起算 time/space,問「最 inner loop 跑幾次?」「遞迴深度?」「有沒有重複計算可以記憶化?」
6. **回顧**:鼓勵用戶把 insight 寫進 `Note{ID}.md`(若無則建議建立)

**觸發條件**(SKILL.md description 寫法):
> 用於 LeetCode/算法題的引導式解題。當用戶詢問「怎麼想」「卡住了」「幫我推一下」「greedy 怎麼證」「DP 狀態怎麼設」、或明確 `/socratic-tutor`、或開啟新題 `Note{ID}.md` 想填內容時觸發。**不直接給答案**;若用戶說「直接告訴我答案」「不要 socratic」則退出此 skill。

**與 TUI 的關係**:解耦。TUI 不依賴 skill;skill 不依賴 TUI。但 TUI 在 scaffold 後印一行提示「想要引導式解題?在 Claude Code 內輸入 `/socratic-tutor <path>`」。

---

## Backlog(本次不做,寫進 `TODO.md`)

用 [project-knowledge-harness] skill 結構,按 priority/effort 標:

| Item | Priority | Effort | 備註 |
|---|---|---|---|
| 結構化 problems metadata(per-problem `meta.json` 或 `problems.toml`) | P1 | M | 解鎖 README 自動 regenerate、mkdocs 索引、stats |
| `leet readme-update` 真正寫檔(取代 `leet readme-row`) | P1 | S | 需要先有 metadata 或 README marker comments |
| CI:Travis → GitHub Actions(matrix Py 3.11/3.12)+ ruff + pre-commit + Go test for `tools/leet` | P1 | S | Travis 已停用免費 OSS,早晚要遷 |
| mkdocs site(用 `mkdocs-site-bootstrap` skill 已備好) | P2 | M | 含 zh-TW 翻譯選項;需先有 metadata |
| Weekly Contest 結構化(統一加 sample tests + README rows) | P2 | M | 用戶說「先維持現狀後續再結構化」 |
| 舊題程式碼現代化(Python 3.11+ 語法、type hints、補缺失 test) | P3 | XL | 600+ 題,逐題或抽樣 |
| 「Do it again」spaced-repetition queue(讀 README Remark 欄 `do it again` / `testcase` 標記) | P2 | S | 與 socratic-tutor 配合 |
| 個人 stats dashboard(Bubble Tea 頁面:每月解題數、category 分佈) | P3 | S | metadata 完成後做 |
| `leet sync`:對 LeetCode profile 拉取已解列表,標 README 缺口 | P3 | M | 需要 auth |
| 考慮 cron / `/schedule` 整合自動推 daily 提醒 | P3 | S | 可選 |
| JavaScript / C++ 子目錄真實啟用(目前只有資料夾預留) | P4 | XL | 等真的有需求再說;`leet` 可加 `--lang js` flag 預留 |
| 把 `leet` binary 發到 Homebrew tap | P3 | S | `goreleaser` 配置 |

---

## Brainstorm — 你沒提到但可能不錯的點子

1. **「複習模式」** — `leet review` 子命令:從 README Remark 欄抓所有 `do it again` / `testcase` 標記的題,隨機抽一題,在 TUI **隱藏現有解答**(只顯示題目),要求重寫。寫完比對舊解法 diff(Lipgloss 雙欄渲染)。
2. **Pre-commit 鎖防止破壞慣例** — 輕量 Python 或 Go pre-commit hook 檢查:
   - `Python3/{Category}/{Folder}/` 內新加的 .py 檔名是否含問題 ID
   - `test_{ID}.py` 是否存在(若有 solution 卻沒 test 就警告)
   - 不阻擋,只警告
3. **Bubble Tea 內 inline `claude` 調用** — submit 成功後,選 `Explain` 鍵,內部 `tea.ExecProcess` 跑 `claude /socratic-tutor --review {path}`,結束回到 TUI。
4. **Note auto-skeleton** — scaffold 時 `Note{ID}.md` 預填 LeetCode 給的 hints + tags + 空白章節(Intuition / Approach / Complexity / Edge cases),降低寫筆記摩擦。
5. **失敗 case 自動 minimize** — submit 失敗拿到 input 後,跑簡單 shrinking(若是 list,試 halve;若是 number,試二分)找最小重現。
6. **CLAUDE.md** — 補一份 repo 的 CLAUDE.md 寫明慣例(資料夾命名、test 結構、Note 格式、`leet` TUI 用法、socratic-tutor 觸發條件),讓未來 agent session 不用重新探索。
7. **Glamour 主題自訂** — 用戶慣用的 markdown 渲染色票,在 `~/.config/leet/style.json` 自訂(直接借用 Glamour 內建的 dark/light/dracula)。

---

## Critical Files(本次會新增/修改)

**新增**:
- `tools/leet/go.mod`、`go.sum`、`Makefile`、`README.md`
- `tools/leet/cmd/leet/main.go`
- `tools/leet/internal/cli/{auth,daily,contest,submit,test,readme,tui}.go`
- `tools/leet/internal/tui/{app,list,detail,editor,result,scaffold_form,styles}.go`
- `tools/leet/internal/leetcode/{api,queries,types,pollers}.go`
- `tools/leet/internal/auth/{store,browser}.go`
- `tools/leet/internal/scaffold/{gen,templates,pascalcase}.go`
- `tools/leet/internal/categories/map.go`
- `tools/leet/internal/readme/row.go`
- `tools/leet/internal/editor/launch.go`
- `tools/leet/testdata/{daily_response,contest_response}.json`
- `tools/leet/internal/scaffold/templates_test.go`、`internal/categories/map_test.go`、`internal/readme/row_test.go`(table-driven Go tests)
- `.claude/skills/socratic-tutor/SKILL.md`
- `.claude/skills/socratic-tutor/reference/{greedy_proofs,dp_state_design,complexity_cheatsheet}.md`
- `TODO.md`(repo 根,backlog index)
- `CLAUDE.md`(repo 根,記錄慣例與 `leet` 用法)
- `.gitignore`:加 `tools/leet/leet`(build artifact)、`tools/leet/dist/`

**參考、不修改**:
- `README.md`(用 `leet readme-row` 印出建議 row,人工貼)
- `Python3/Array/MatrixDiagonalSum/test_1572.py`(test 慣例 reference)
- `Python3/Math/PowerOfFour/`(多解 reference,5 個 strategy 檔)
- `Contest/LeetCodeWeeklyContest/WeeklyContest344/`(contest 結構 reference)
- `requirements.txt`(暫不動)
- `.travis.yml`(暫不動,等 backlog CI 遷移)

---

## Verification Plan

**A. TUI(`tools/leet/`)**:
1. `cd tools/leet && go build -o leet ./cmd/leet && go install ./cmd/leet`(或 `make install`)
2. `leet auth` → 貼測試帳號 cookie → 確認 `leet auth --check` 顯示 logged in
3. `leet daily --no-edit` → 確認:
   - 新資料夾出現在正確 `Python3/{Category}/`(category 推導正確)
   - `Naive{ID}.py` 含 LeetCode starter `class Solution` skeleton
   - `test_{ID}.py` 含 `testcases = [...]`(LeetCode sample 至少 1 case)+ `def test_Naive():`
4. 手寫一個錯解 → `leet submit Python3/.../{folder}/Naive{ID}.py` → 確認:
   - verdict 顯示 Wrong Answer
   - `cases/failed_YYYYMMDD.txt` 已產生(含 input + expected + got)
5. 改正解 → `leet submit` 通過 → `leet readme-row` 印出建議 row
6. `leet contest weekly --latest` → 確認 4 個子資料夾與 sample 都建好
7. `leet tui` → 互動測試:
   - 列表載入流暢(<200ms)
   - 選題開 `$EDITOR=nvim` 進出無 terminal 殘留(`tea.ExecProcess` 應自動處理)
   - submit 結果面板渲染正確(verdict 顏色、diff 高亮)
   - Ctrl+C / q 乾淨退出
8. `cd tools/leet && go test ./...` → 全綠(scaffold templates / categories map / readme row / 假 GraphQL response)
9. `golangci-lint run`(若已裝)→ 無 warning

**B. Socratic Tutor skill**:
1. 在 Claude Code 內輸入 `/socratic-tutor Python3/Array/MatrixDiagonalSum/`
2. 確認:
   - 不直接給答案
   - 先問用戶第一直覺
   - 漸進提示分 4 級
   - 寫完後主動討論複雜度
3. 對 greedy 題(如 #45 Jump Game II)測試:確認會要求證明
4. 對 DP 題(如 #5 Longest Palindromic Substring)測試:確認會要求 state/transition/base case
5. 用戶說「直接告訴我答案」→ 確認 skill 退出,不繼續 socratic

**C. 不破壞既有**:
1. `pytest --cov=Python3/`(repo 根)→ 既有 600+ 題測試全綠
2. `git diff README.md` → 空(README 未被自動修改)
3. `.travis.yml` 未動
4. `tools/` 之外的檔案 diff 只有 `CLAUDE.md`、`TODO.md`、`.claude/skills/socratic-tutor/`、`.gitignore` 新增

---

## 下一步(用戶確認 plan 後)

1. 建 `tools/leet/` Go module 骨架 + `cmd/leet/main.go` + cobra root → `leet --help` 跑得起來
2. 實作 `internal/leetcode/` GraphQL client(daily/problem queries)+ `internal/auth/` cookie 存取 → `leet auth` 與 `leet daily --no-edit` 跑通
3. 實作 `internal/scaffold/` + `internal/categories/` → daily 真的能落地檔案
4. 實作 `leet submit` + failed case 寫入
5. 實作 `leet contest weekly`
6. 寫 Bubble Tea TUI 包裝以上(list / detail / editor / result / form)
7. 寫 socratic-tutor skill(可與 TUI 並行)
8. 補 CLAUDE.md 與 TODO.md(backlog)
9. 用 1 週實際解每日題試跑,收集摩擦點再迭代

預估 effort:
- 骨架 + auth + daily + scaffold:1 個 evening
- submit + contest:1 個 evening
- Bubble Tea TUI:2-3 個 evening(主要在 polish 與 keymap)
- socratic-tutor skill:0.5 day
- 總計 ~1 週 sparse work
