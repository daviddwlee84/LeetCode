# LeetCode Repo Refactor — Phases 1 & 2

> **Phase 1** landed in commit `06064da` (2026-05-15): Go (Bubble Tea) `leet`
> CLI at `tools/leet/`, `.claude/skills/socratic-tutor/`, CLAUDE.md, TODO.md.
> `leet daily` verified end-to-end against live LeetCode. Phase 1 content
> kept below as the historical record.
>
> **Phase 2** (this update): pre-commit hygiene bootstrap, config-driven
> `leet` (`~/.config/leet/config.toml` + per-repo `.leet/config.toml`),
> `leet init` for fresh practice repos with `legacy` / `structured` layout
> choice, plus online-test / offline-test surface alignment with LeetCode's
> Run vs Submit endpoints.

---

# Phase 1 — TUI + Socratic Tutor (LANDED 2026-05-15)

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

---

# Phase 2 — Pre-commit hygiene + generic `leet` (config-driven) + `leet init` + Run/Submit alignment

## Phase 2 Context

Phase 1 hardcoded one user's conventions:現 `Naive{ID}.py` / `test_{ID}.py` /
`Note{ID}.md` 命名、12 個分類資料夾、Python3 路徑全寫在 Go 程式碼裡。雖然
試跑成功了,但有 4 個遺留問題:

1. **別人裝不了**:`go install` 雖然可行,但 binary 把這個 repo 的 8 年慣
   例 hardcode 死,別人下了也只能跟著用一模一樣的命名。
2. **未來自己想換結構也綁住**:TODO.md 已寫好 P2 想把命名改成「資料夾級
   README + 無 ID 檔名 + `meta.json`」,但現在每個 scaffold 路徑都是 const
   string,改動牽連大。
3. **沒辦法在 temp folder mock 測試 layout 行為**:integration test 想驗證
   兩種 layout 都 OK,但程式碼沒有「layout」這個概念可以注入。
4. **online test 缺漏**:LeetCode UI 有 "Run"(不計 submission)和 "Submit"
   兩個按鈕,Phase 1 只實作後者。寫完想先用 sample 跑一下不留 submission
   紀錄的需求沒被覆蓋到。

加上 Phase 1 commit 之前未啟用 pre-commit / gitleaks,後續 daily session 不
建議裸 commit。

Phase 2 目標:

- 把 hygiene 補上(一次性執行 `bootstrap-project.sh`)
- 把 `leet` 全面 config-driven,既支援這個 repo 的 legacy 結構、也支援未來
  的 structured 結構,兩者**共用同一 binary**
- 加 `leet init` 讓別人能用同個工具開新的練習 repo
- 對齊 LeetCode Run/Submit 兩個 endpoint,加 `leet test --online`

## 鎖定的設計決策(已與用戶確認)

| 決策 | 答案 |
|---|---|
| Layout 命名 | `legacy` / `structured` |
| Structured 的 ID 存哪 | `meta.json` |
| Structured 的 test 怎麼寫 | 單一 `test.py` + `pytest.mark.parametrize` 跨 strategies |
| Structured case 風格 | **資料夾 kebab-case**(對齊 LeetCode URL slug)+ **檔名 snake_case**(Python 不允許 hyphen)+ **top-level category 也小寫**(`Python3/array/` 而非 `Python3/Array/`) |
| Strategy 來源分類 | **三類** `kind`: `own`(原創)/ `reference`(看了 hint 後自己重寫)/ `archive`(純收藏別人的解法,供查閱)— 全部都過 test,但 TUI / review 模式可按 kind 過濾 |
| Agent 設定路徑 | **`.agents/`** 只放通用內容(`skills/`);**tool-specific** 設定(`.claude/settings.json` 等)留在原本工具自己的目錄。`.claude/skills`、`.claude/plans` 變 symlink 進 `.agents/`;`.claude/settings.json` 維持實體檔。未來新增 Cursor / OpenCode 也比照(自己的 settings 留各自目錄,符號連 shared 內容) |
| 主 agent 說明檔 | `AGENTS.md` 為實體檔(業界 emerging convention),`CLAUDE.md` 為 symlink → `AGENTS.md` |
| 這個 repo 怎麼設 layout | 顯式寫 `.leet/config.toml` 鎖 `layout = "legacy"`(不靠 auto-detect) |

---

## A. 一次性執行 `bootstrap-project.sh`

`bash /Users/daviddwlee84/.claude/skills/agent-history-hygiene/scripts/bootstrap-project.sh --install-hook`

會做的事(dry-run 已驗證):

- `.pre-commit-config.yaml`(redact-agent-secrets + gitleaks + 標準 hygiene
  hooks)
- `.gitleaks.toml`(含 LeetCode 場景:`LEETCODE_SESSION`、JWT、64-char hex
  csrftoken)
- `scripts/redact_secrets.py`(redactor;chezmoi 上游 sync 路徑在 skill
  reference 裡)
- `pre-commit install`(裝 git hook)
- `--install-hook`:加 `prepare-commit-msg` hook 自動 stage 當前 SpecStory
  session + 最新 plan 檔
- Audit `~/.claude/settings.json`:warn 若沒設 `plansDirectory`

完成後,後續 `git commit` 會自動跑 redact → gitleaks,沒過不能 commit。
這個 sub-deliverable 不寫程式碼、不需要規劃,跑一次完成。

---

## B. Config-driven `leet`(主要工作)

### B.1 Config schema

**`~/.config/leet/config.toml`**(per-user 預設):

```toml
# Default layout for new repos when `leet init` is called without --layout.
default_layout = "structured"

# Where to look for auth cookies (file path, mode 0600). Default already
# correct for macOS; expose for portability.
auth_file = "~/Library/Application Support/leet/auth.toml"

# Default category list — can be overridden per-repo.
categories = [
  "Array", "BinaryTree", "BitManipulation", "Design",
  "DynamicProgramming", "Graph", "Interactive", "LinkedList",
  "Math", "Search", "String", "AdHoc",
]
fallback_category = "AdHoc"

# Priority table for LeetCode tag → category folder.
[[category_priority]]
tag = "Linked List"
dir = "LinkedList"
# ... 22 more entries (current internal/categories/map.go content)

[layouts.legacy]
folder_pattern   = "{title_pascal}"
solution_pattern = "{strategy}{id}.py"
test_pattern     = "test_{id}.py"
note_pattern     = "Note{id}.md"
test_import      = "from {strategy}{id} import Solution as {strategy}"
test_style       = "per_strategy"     # one def test_X per strategy
meta_file        = ""                 # no meta.json in legacy

[layouts.structured]
folder_pattern   = "{title_kebab}"          # "matrix-diagonal-sum"
category_case    = "lower"                  # "array" not "Array"
solution_pattern = "{strategy_snake}.py"    # "hash_table.py"
test_pattern     = "test.py"
note_pattern     = "README.md"
test_import      = "from {strategy_snake} import Solution as {strategy_camel}"
test_style       = "parametrize"            # single test.py + pytest.mark.parametrize
meta_file        = "meta.json"
strategy_kinds   = ["own", "reference", "archive"]

[paths]
python    = "Python3"
contest   = "Contest/LeetCodeWeeklyContest"
# Future: javascript = "JavaScript", cpp = "Cpp"
```

Token substitution helpers in `internal/config/expand.go`:

| Token | Example: "Matrix Diagonal Sum" / strategy "HashTable" |
|---|---|
| `{title_pascal}` | `MatrixDiagonalSum` (legacy folder) |
| `{title_kebab}` | `matrix-diagonal-sum` (structured folder, = LeetCode slug) |
| `{strategy}` | `HashTable` (legacy file prefix) |
| `{strategy_snake}` | `hash_table` (structured file stem) |
| `{strategy_camel}` | `HashTable` (test import `as` name) |
| `{id}` | `1572` |

**`.leet/config.toml`**(per-repo,覆蓋 user-level)。對**這個 repo**只寫:

```toml
layout = "legacy"
# Everything else inherits from user-level / built-in defaults.
```

新 repo 透過 `leet init --layout=structured` 產生的 `.leet/config.toml`:

```toml
layout = "structured"
```

### B.2 Resolution order

由 high to low precedence:

1. CLI flag(`--layout=structured`)
2. Per-repo `.leet/config.toml`
3. Per-user `~/.config/leet/config.toml`
4. Built-in defaults(寫死在 binary,= 現在 hardcode 內容,確保 zero-config 可跑)

### B.3 Code changes

**新增**:

- `tools/leet/internal/config/`
  - `config.go` — `Config` struct(含 `Layout`, `Categories`, `Priority`,
    `Paths`)、`Load(repoRoot)` 函式(走 resolution order)
  - `defaults.go` — built-in defaults(從現有 hardcode 移過來)
  - `merge.go` — overlay logic
  - `expand.go` — pattern substitution(`{strategy}{id}` → `"Naive1572"`)
  - `config_test.go` — table-driven test 各種 overlay 情境

**重構**:

- `internal/categories/map.go` — 改成 `PickFromConfig(cfg, tags) string`,
  priority 表從 config 來;保留 `PickCategory(tags)` 當預設值的 thin
  wrapper(向後相容測試)
- `internal/scaffold/gen.go` — `Daily(cfg, in)` 與 `DailyFromQuestion(cfg,
  folder, q, withNote)`;檔名/folder pattern 都從 `cfg.Layout` 來
- `internal/scaffold/templates.go` — 拆成 `templates_legacy.go` 與
  `templates_structured.go`(structured 的 `test.py` 用 parametrize 樣板)
- `internal/scaffold/gen.go::InspectFolder` — 兩種 layout 都要能讀:legacy
  從檔名抽 ID,structured 從 `meta.json` 讀 ID;readme-row 命令兩種都要動
- `internal/cli/daily.go`、`contest.go`、`submit.go`、`readme.go` — 都先
  `cfg := config.Load(repoRoot)` 再傳給 scaffold/categories
- `internal/cli/repo.go::findRepoRoot` — 同時偵測 `.leet/` 或 `.git/`,
  `.leet/` 優先(允許不在 git 內的練習 repo)

**Structured 的 `meta.json` schema**(寫進 `internal/scaffold/meta.go`):

```json
{
  "id": "1572",
  "title": "Matrix Diagonal Sum",
  "title_slug": "matrix-diagonal-sum",
  "difficulty": "Easy",
  "tags": ["Array", "Math"],
  "url": "https://leetcode.com/problems/matrix-diagonal-sum/",
  "date_added": "2026-05-15",
  "leetcode_question_id": "1726",
  "strategies": [
    {
      "file": "naive.py",
      "name": "Naive",
      "kind": "own",
      "created": "2026-05-15",
      "complexity": {"time": "O(n)", "space": "O(n)"},
      "notes": ""
    },
    {
      "file": "better.py",
      "name": "Better",
      "kind": "own",
      "created": "2026-05-16",
      "complexity": {"time": "O(n)", "space": "O(1)"},
      "notes": "After noticing the indices overlap on odd-sized matrices"
    },
    {
      "file": "elegant.py",
      "name": "Elegant",
      "kind": "archive",
      "created": "2026-05-17",
      "source": "leetcode editorial",
      "complexity": {"time": "O(n)", "space": "O(1)"},
      "notes": "Beautiful one-liner I want to study"
    }
  ]
}
```

**Strategy `kind` 三類**(用戶確認):

- `own` — 原創,自己想出來的
- `reference` — 看了 hint / discussion / editorial 之後自己重寫
- `archive` — 純收藏別人的解法,**不混淆認知**(過 test、可查閱,但明確不是「我做的」)

CLI 在 `leet add-strategy` / `leet tui` / 未來的 `leet review` 都會用到:

- `leet review` 預設只挑 `kind=own` 跟 `kind=reference` 的題目要求重做,跳過
  `archive`(收藏目的非鍛鍊)
- `leet tui` 列表加 icon:`✓ own` / `↪ reference` / `⤵ archive`

### B.4 重構期 backward compatibility

這個 repo 透過 `.leet/config.toml` 鎖 `layout = "legacy"`,所以:

- `leet daily` 跑出來還是 `Naive1572.py` + `test_1572.py`(行為不變)
- 既有 600+ 題目資料夾不動
- README 不動
- `leet readme-row` 對舊資料夾也照常運作(從檔名抽 ID)

---

## C. `leet init`(新指令)

### C.1 用法

```sh
leet init [target-dir] \
  [--layout=legacy|structured] \
  [--languages=python,javascript,cpp] \
  [--no-git] \
  [--no-readme] \
  [--with-claude-md] \
  [--with-socratic-skill] \
  [--non-interactive]
```

預設互動式(Huh form):

1. Target dir(default `.`,若已是 git repo 或已有 `.leet/` 則 abort 並提示
   `--force`)
2. Layout(legacy / structured,default structured)
3. Languages(預設 Python3 only,可加 JavaScript、Cpp — 目前只 Python3
   起作用,其他兩個 Phase 2 只建空資料夾預留)
4. Categories(default 12 / minimal {Array, String, BinaryTree, DP, Graph,
   AdHoc} / custom — open `$EDITOR` 編輯 toml)
5. Init git?(default yes)
6. 寫 CLAUDE.md / 加 socratic-tutor skill?(default both yes)

### C.2 產出(structured layout 預設)

```
<target>/
├── .git/                   (若 init git)
├── .gitignore              (Python + Go + leet cases;以 chezmoi 的 Python
│                            .gitignore 為基礎)
├── .leet/
│   └── config.toml         (layout=structured + paths,其他繼承 user-level)
├── Python3/
│   ├── array/.gitkeep            (小寫!structured layout)
│   ├── binary-tree/.gitkeep
│   ├── dynamic-programming/.gitkeep
│   └── ... (chosen categories,每個含 .gitkeep)
├── Contest/
│   └── .gitkeep
├── README.md                       (template:title + table header,空表)
├── AGENTS.md                       (主 agent 說明檔,實體檔)
├── CLAUDE.md → AGENTS.md           (symlink,相容 Claude Code)
├── .agents/                        (通用,實體)
│   ├── skills/
│   │   └── socratic-tutor/         (optional;symlink 到 user-global 或 copy)
└── .claude/                        (Claude Code-specific,實體目錄)
    ├── settings.json               (含 plansDirectory = "./.claude/plans")
    └── skills → ../.agents/skills  (symlink)
```

**為什麼這樣切**:

- `settings.json` 是 Claude Code 專屬格式(plansDirectory、hooks 等),其他
  工具不認 → 留在 `.claude/` 是實體檔
- `skills/` 是相對通用內容(`SKILL.md` 業界已有共識
  是純 markdown)→ 用 symlink 共享給 `.agents/`,未來 Cursor `.cursor/skills`
  也比照
  `.claude/plans` 是 symlink,實際落到 `.agents/plans/` — 對 Claude 透明

Legacy layout 產出差異:

- `Python3/Array/`、`Python3/BinaryTree/`(PascalCase)
- 無 `meta.json` schema 預設
- 其餘相同(`.agents/` + `AGENTS.md` + symlinks 不分 layout 都這樣)

### C.3 Code changes

**新增**:

- `tools/leet/internal/cli/init.go` — cobra subcommand,Huh form,呼叫
  `scaffold.InitRepo`
- `tools/leet/internal/scaffold/repo_init.go` — `InitRepo(opts) error`,
  做 `mkdir -p`、寫 templates、`git init`(若需要)、建 symlink
  (`.claude → .agents`、`CLAUDE.md → AGENTS.md`,用 `os.Symlink` 走相對路徑)
- `tools/leet/internal/scaffold/init_templates.go` — embed 的 README /
  AGENTS.md / .gitignore / `.agents/settings.json` template
- `tools/leet/internal/scaffold/repo_init_test.go` — 在 `t.TempDir()` 跑兩
  種 layout 各一次,assert 檔案存在 + symlinks 正確指向

### C.4 Symlink 與 git 行為

- Git 預設追蹤 symlink(`mode 120000`),不是檔案內容
- macOS / Linux 工作正常;Windows 預設要 admin 才能建 symlink → `leet init`
  在 Windows 上偵測失敗時,改用 **junction**(`mklink /J`)或印警告改寫實
  體檔(本 repo 是 macOS,暫不深挖)
- `.gitignore` 不需特別處理 symlink — git 看到的是 link 本身

### C.5 這個 repo 的搬遷(Phase 2 的 sub-task)

當前 repo 已有 `.claude/{plans,skills,settings.json}` 跟剛寫的 `CLAUDE.md`。
Phase 2 要做(注意只搬通用內容):

```sh
# 1. 建 .agents/ 並把通用內容搬過去
mkdir -p .agents
git mv .claude/skills .agents/skills
# .claude/settings.json 留在原地(實體檔,Claude-specific)

# 2. 在 .claude/ 建 symlinks 回指
ln -s ../.agents/skills .claude/skills
git add .claude/skills

# 3. CLAUDE.md → AGENTS.md + symlink
git mv CLAUDE.md AGENTS.md
ln -s AGENTS.md CLAUDE.md
git add CLAUDE.md
```

驗證:

- `ls -la .claude/` → 看到 `settings.json`(實體)
  - `skills → ../.agents/skills`
- `readlink .claude/plans` 印 `../.agents/plans`
- `cat .claude/skills/socratic-tutor/SKILL.md` → 跟
  `cat .agents/skills/socratic-tutor/SKILL.md` 一樣(symlink 透明)
- `cat CLAUDE.md` → 跟 `cat AGENTS.md` 一樣
- 新一次 Claude Code session 跑 `/plan` 或叫起 `/socratic-tutor` 都能正常 —
- `git status` 看 plans/skills 顯示為 typechange(file → symlink),不是
  「整個資料夾被刪」

---

## D. Run vs Submit(online/offline test 對齊)

### D.1 LeetCode 兩個 endpoint 對比

| Action | Endpoint | 計入 stats | 用途 |
|---|---|---|---|
| Run(LeetCode UI) | `POST /problems/{slug}/interpret_solution/` | 否 | 用 sample input 或 custom input 跑一次拿 stdout |
| Submit(LeetCode UI) | `POST /problems/{slug}/submit/` | 是 | 計 submission,跑全部 hidden tests |

兩個 endpoint 都需要 `LEETCODE_SESSION` + `csrftoken`。Run 不算 submission
所以可以隨意快速試。

### D.2 Command surface

| 命令 | 行為 | Phase |
|---|---|---|
| `leet test [path]` | 本地 pytest(現有) | 1(沿用) |
| `leet test --online [path]` | LeetCode interpret_solution 跑 default sample,顯示 stdout 與 verdict(Accepted / Wrong Answer / Runtime Error) | 2 新增 |
| `leet test --online --case "[1,2,3]\n5"` | 同上但用 custom input | 2 新增 |
| `leet test --online --watch` | 開 fsnotify 監聽該檔,存檔自動再跑一次 | 2 stretch goal |
| `leet submit [path]` | submit 真正提交(現有) | 1(沿用) |

### D.3 Code changes

**新增**:

- `internal/leetcode/interpret.go` — `InterpretSolution(ctx, slug, lang,
  code, dataInput) (InterpretResult, error)`,POST 後 poll
  `/submissions/detail/{id}/check/`(跟 submit 流程相同,只是 endpoint 換掉)
- `internal/leetcode/queries.go` — 加 `queryQuestionDataMeta` 拿 default
  `sampleTestCase`(若 user 沒 `--case`,用 LeetCode 預設 sample)
- `internal/leetcode/types.go` — `InterpretResult` struct(`StatusCode`,
  `StatusMsg`, `CodeAnswer`, `ExpectedCodeAnswer`, `Runtime`, ...)

**重構**:

- `internal/cli/test.go` — 加 `--online` / `--case` / `--watch` flag;
  `--online` 走新的 interpret 路徑,否則沿用現在的 pytest wrapper
- `internal/leetcode/pollers.go` — 把現有 `PollResult` 抽出可重用部分
  (`pollSubmissionCheck`),submit 與 interpret 共用

### D.4 與 fail-case capture 的整合

`leet test --online` Wrong Answer 時也寫入 `cases/failed_*.txt`(跟 submit
同樣的 capture 邏輯,但檔名前綴改 `online_failed_YYYYMMDD.txt` 跟 submission
分開,避免誤以為是真正失敗)。

---

## E2. Shell completion(`leet completion install`)

### E2.1 為什麼

Cobra 已自動生成 `leet completion zsh|bash|fish|powershell` 印出 completion
script(已在 `leet --help` 看到 `completion` subcommand)。缺的是讓使用者不
用想「該存到哪個檔」「.zshrc 要不要改」。`leet completion install` 自動處
理 shell-specific path + 提示。

### E2.2 行為

| Shell | 偵測 | 預設路徑 | .rc 需求 |
|---|---|---|---|
| zsh | `$ZSH_VERSION` 或 `$SHELL` 含 `zsh` | `~/.zfunc/_leet` | `fpath=(~/.zfunc $fpath); autoload -U compinit; compinit` 在 `.zshrc`(若已有則不重複) |
| bash | `$BASH_VERSION` 或 `$SHELL` 含 `bash` | `~/.bash_completion.d/leet`(或 `~/.local/share/bash-completion/completions/leet` if XDG set) | source via standard bash-completion |
| fish | `$SHELL` 含 `fish` | `~/.config/fish/completions/leet.fish` | 無 |

### E2.3 用法

```sh
leet completion install              # auto-detect shell
leet completion install --shell=zsh  # explicit
leet completion install --print      # 印到 stdout 不寫檔(同 cobra 既有)
```

執行後:

1. 偵測 shell
2. `mkdir -p` 目標目錄
3. 寫檔
4. **若是 zsh 且 `.zshrc` 沒有 `fpath=(~/.zfunc ...)` 設定**,印一段
   one-liner 提示用戶 append(不自動改 `.zshrc`,避免不可逆動作)
5. 印「reload your shell or run `exec zsh` to activate」

### E2.4 Code changes

**新增**:

- `internal/cli/completion_install.go` — 註冊為 `completion install`
  subcommand(在 cobra 生成的 `completion` 下面加 child),呼叫
  `cmd.Root().GenZshCompletion(file)` 等 cobra API

**測試**:

- `internal/cli/completion_install_test.go` — table-driven,用 `t.TempDir()`
  覆寫 home dir,驗證每種 shell 寫到正確路徑

預估 effort:30 分鐘。可在 Phase 2.D 之後順手做。

---

## E. Mock testing infrastructure(用 temp folder)

### E.1 為什麼

設計重點是「兩種 layout 都能驗證」。靠真實 LeetCode 跑會有 rate limit、auth
要求、且每天 daily 不同無法 reproducible。Mock 才能在 CI 跟本地 `go test`
之間一致。

### E.2 結構

新增 `tools/leet/internal/leetcode/mocks_test.go`:

- `func MockServer(t testing.TB) (url string, cleanup func())`
- 內含路由表:`/graphql` → 根據 query name 回 testdata fixture;
  `/problems/{slug}/submit/` → 回固定 submission_id;
  `/submissions/detail/{id}/check/` → 第一次回 PENDING,第二次回 SUCCESS

新增 `tools/leet/testdata/`:

- `daily_response.json`(Phase 1 plan 已留 slot)
- `question_data_two_sum.json`
- `interpret_response_accepted.json`
- `interpret_response_wrong.json`
- `submit_check_accepted.json`
- `submit_check_wrong.json`

新增 `tools/leet/internal/leetcode/api.go` 改動:加 `BaseURL` 可注入(用
`NewClient(creds, opts ...Option)` 風格,或加 `WithBaseURL(url)`),讓
mock server URL 能塞進去。

### E.3 整合測試

新增 `tools/leet/internal/cli/integration_test.go`:

```go
func TestInitDailyLegacy(t *testing.T) {
    repo := t.TempDir()
    runLeet(t, repo, "init", "--layout=legacy", "--non-interactive")
    srv, cleanup := leetcode.MockServer(t); defer cleanup()
    t.Setenv("LEET_BASE_URL", srv.URL)
    runLeet(t, repo, "daily", "--no-edit")
    assert.FileExists(t, filepath.Join(repo, "Python3/Search/FindMin.../Naive153.py"))
}

func TestInitDailyStructured(t *testing.T) {
    // ... same but assert Naive.py + meta.json + test.py with parametrize
}

func TestOnlineTestWrongAnswer(t *testing.T) {
    // mock interpret returns wrong; assert cases/online_failed_*.txt written
}
```

---

## F0. `requirements.txt` → `pyproject.toml` + `uv`

### F0.1 為什麼

現在 `requirements.txt` 只有 4 行(pytest / pytest-cov / coverage / numpy),
無 pin、無 dev-only 區分、無 ruff/lint 配置位置、Python 版本只在 `.travis.yml`
裡記。升級到 `pyproject.toml` + `uv`:

- 單一 source of truth(project metadata + deps + tool config 都在一份檔)
- `uv.lock` 鎖確切版本 → 重現性
- `uv sync` 1 秒裝完 `.venv/`
- ruff / pytest / coverage config 都搬進來,免除 `.coveragerc` 額外檔
- 與將來 Phase 3 CI 遷移(GH Actions `uv run pytest`)無縫銜接

### F0.2 產出

新增 `pyproject.toml`:

```toml
[project]
name = "leetcode-practice"
version = "0.1.0"
description = "Personal LeetCode algorithm practice archive"
requires-python = ">=3.11"
dependencies = [
    "numpy>=1.26",     # used by some grid/matrix problems
]

[dependency-groups]
dev = [
    "pytest>=8.0",
    "pytest-cov>=5.0",
    "coverage>=7.4",
    "ruff>=0.5",
]

[tool.pytest.ini_options]
testpaths = ["Python3"]
python_files = ["test_*.py", "test.py"]    # legacy + structured both
addopts = "-q --tb=short"

[tool.coverage.run]
source = ["Python3"]
omit = ["**/test_*.py", "**/test.py"]

[tool.ruff]
line-length = 100
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "I", "B", "UP", "SIM"]
ignore = ["E501"]    # Note*.md content lines occasionally show long URLs in py
```

刪除:

- `requirements.txt`(內容已搬進 `[dependency-groups]`)
- `.coveragerc`(內容已搬進 `[tool.coverage.run]`)

新增 `uv.lock`(自動,`uv sync` 跑一次產生)。

### F0.3 onboarding 變化

| 之前 | 之後 |
|---|---|
| `python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt` | `uv sync` |
| `pytest --cov-report term --cov Python3/` | `uv run pytest`(配置都在 pyproject)|
| 無 lint | `uv run ruff check` / `uv run ruff format` |

README.md 對應段也要從 `pip install -r requirements.txt` 改成 `uv sync`,
並提一句「想用純 pip 也可以:`pip install -e ".[dev]"`」(PEP 735 在 pip 24+
原生支援 dependency-groups,沒 uv 的用戶也能裝)。

### F0.4 與 leet 工具的整合

新增 `leet init` 預設也產這份 pyproject.toml(隨 layout 不變),這樣別人
init 出來的新 repo 也是現代 setup。`internal/scaffold/init_templates.go`
embed 這份 template。

### F0.5 與這個 repo 既有測試的相容性

- 既有 600+ 題的 `test_*.py` 全部沿用 → `[tool.pytest.ini_options]` 的
  `python_files` 涵蓋 `test_*.py`(legacy)跟 `test.py`(structured 未來)
- `.travis.yml` 暫時保留(等 Phase 3 CI 遷移時一起改)。Travis 可以先沿用
  `pip install -r requirements.txt`,要不要保留 requirements.txt 在 Phase 2
  決定一次:
  - **建議刪掉,Travis 改用 `uv sync && uv run pytest`**(Travis 支援 uv)
  - 或保留 requirements.txt 當 shim 直到 Travis 廢棄

---

## F. Backlog adjustments(從 Phase 1 backlog 移除已做 / 重排)

進到 Phase 2 後,TODO.md 要更新:

- 移除「`~/.config/leet/config.toml`」獨立條目(本 Phase 含進去了)
- 移除「`leet init`」獨立條目(本 Phase 含進去了)
- 「Folder-level README convention shift」改成「**migration script** for
  legacy → structured」(layout 已支援,差實際 migrate)
- 新增「`leet test --online --watch` polish」P3
- 新增「Mock test fixtures 擴充 to cover contest endpoints」P3

---

## Critical files

**新增**:

- `tools/leet/internal/config/config.go`, `defaults.go`, `merge.go`,
  `expand.go`(含 kebab / snake / camel / pascal converters), `config_test.go`
- `tools/leet/internal/scaffold/repo_init.go`, `init_templates.go`,
  `meta.go`(meta.json reader/writer,含 strategies + kind), `templates_structured.go`,
  `repo_init_test.go`
- `tools/leet/internal/cli/init.go`
- `tools/leet/internal/cli/completion_install.go`
- `tools/leet/internal/cli/integration_test.go`
- `tools/leet/internal/leetcode/interpret.go`, `mocks_test.go`
- `tools/leet/testdata/*.json`(6 個 fixture)
- `.leet/config.toml`(這個 repo 鎖 `layout = "legacy"`)
- `.pre-commit-config.yaml`, `.gitleaks.toml`, `scripts/redact_secrets.py`
  (bootstrap-project.sh 產出)

**搬遷(本 repo Phase 2 完成)**:

- `.claude/skills` 內容 → `.agents/skills/`(實體)+ `.claude/skills` symlink
- `.claude/settings.json` 不動(Claude-specific,實體留原處)
- `CLAUDE.md` → `AGENTS.md`(實體)+ `CLAUDE.md` symlink
- `requirements.txt` + `.coveragerc` → `pyproject.toml` + (產) `uv.lock`

**重構**:

- `tools/leet/internal/categories/map.go` — accept config-driven priority
- `tools/leet/internal/scaffold/gen.go`, `templates.go` — config-driven
- `tools/leet/internal/scaffold/gen.go::InspectFolder` — 兩種 layout 都讀
- `tools/leet/internal/cli/{daily,contest,submit,readme,test}.go` — load
  config 並傳給 scaffold/categories
- `tools/leet/internal/cli/repo.go::findRepoRoot` — `.leet/` 優先於 `.git/`
- `tools/leet/internal/leetcode/api.go` — `BaseURL` 可注入
- `tools/leet/internal/leetcode/pollers.go` — 抽 `pollSubmissionCheck` 共用

**參考、不修改**:

- 既有 600+ 題目資料夾(legacy layout,跟新 binary 完全相容)
- `README.md`(本 repo 主 readme,不動)
- `.travis.yml`(等 Phase 3 CI 遷移)

---

## Verification plan

### Phase 2.A — bootstrap-project

1. `bash .../bootstrap-project.sh --install-hook` 跑完
2. 確認 `.pre-commit-config.yaml`、`.gitleaks.toml`、`scripts/redact_secrets.py`
   都存在,且權限正常
3. `pre-commit run --all-files`(在 clean checkout 上)→ 全綠或只有預期的
   format-only 修正
4. 故意 stage 一個含假 cookie 的 `.specstory` 檔 → `git commit` 應該被擋

### Phase 2.A2 — 本 repo 搬遷(symlinks + pyproject.toml)

1. `.agents/skills/` 存在(實體)
2. `.claude/plans` 與 `.claude/skills` 是 symlink:
   - `readlink .claude/skills` 印 `../.agents/skills`
3. `.claude/settings.json` 仍是實體檔(`file ...` 不顯示 symlink)
4. `CLAUDE.md` symlink → `AGENTS.md`(`readlink CLAUDE.md` 印 `AGENTS.md`)
5. 新 Claude Code session:
   - 跑 `/plan` 寫進的檔出現在 `.agents/plans/`(實際落點)
   - `/socratic-tutor` 仍正常觸發(skill 透過 symlink 讀到)
6. `git status` 顯示 `.claude/plans`、`.claude/skills`、`CLAUDE.md` 為
   `typechange`,非 file deletion
7. `uv sync` 在乾淨 checkout 跑通,產 `.venv/` + `uv.lock`
8. `uv run pytest` 跑既有 600+ 題全綠
9. `git status` 顯示 `requirements.txt`、`.coveragerc` 已刪、`pyproject.toml`
   已加

### Phase 2.B — config-driven leet (這個 repo,legacy layout 不變)

1. 寫 `.leet/config.toml` `layout = "legacy"`
2. `cd tools/leet && go test ./...` 全綠(含新的 config_test 跟 integration)
3. `leet daily --no-edit --repo-root /tmp/legacyTest`(同 Phase 1 smoke)→
   產出檔名仍是 `Naive{ID}.py` + `test_{ID}.py`(行為與 Phase 1 一致)
4. `leet readme-row Python3/Array/MatrixDiagonalSum/`(這個 repo 既有題目)
   → 仍印出正確 row

### Phase 2.C — leet init (兩種 layout)

1. `TMP=$(mktemp -d) && leet init "$TMP" --layout=legacy --non-interactive`
   → 確認:
   - `.leet/config.toml` 寫 `layout = "legacy"`
   - 12 個 PascalCase category 資料夾 + .gitkeep(`Python3/Array/`, ...)
   - README.md template、.gitignore、AGENTS.md 都對
   - `.claude` 是 symlink → `.agents`,`CLAUDE.md` 是 symlink → `AGENTS.md`
   - `readlink .claude` 印出 `.agents`
2. `cd $TMP && leet daily --no-edit` → 產 legacy 檔名(`Naive{ID}.py` etc.)
3. `TMP2=$(mktemp -d) && leet init "$TMP2" --layout=structured` →
   - `.leet/config.toml` 寫 `layout = "structured"`
   - 12 個 kebab-case 小寫 category 資料夾(`Python3/array/`,
     `Python3/binary-tree/`, ...)
4. `cd $TMP2 && leet daily --no-edit` → 產:
   - `Python3/search/find-minimum-in-rotated-sorted-array/naive.py`
   - `test.py`(parametrize 跨 strategies)
   - `meta.json`(含 strategies array,Naive 的 `kind=own`)
   - 資料夾根 `README.md`(問題描述)
5. `cat $TMP2/Python3/search/.../meta.json | jq '.strategies[0]'` → 含
   `file`, `name`, `kind=own`, `created` 等欄位

### Phase 2.D — Run vs Submit

1. `leet test Python3/Array/MatrixDiagonalSum/` → 本地 pytest 跑通(現有行為)
2. `leet test --online Python3/Array/MatrixDiagonalSum/Better1572.py` →
   走 interpret_solution,印 stdout + verdict(實測對 LeetCode)
3. 故意改錯一行 → `leet test --online ...` 印 Wrong Answer + 寫
   `cases/online_failed_*.txt`
4. `leet submit ...` 沒有變更行為(仍走 submit endpoint)

### Phase 2.E2 — Shell completion

1. `leet completion install --shell=zsh --print` → 印出 zsh completion script
2. `leet completion install` 在 zsh terminal 內 → 寫 `~/.zfunc/_leet`,提示
   `fpath` 設定(若未設)
3. `exec zsh && leet <TAB>` → 看到 subcommand 補全
4. 用 `t.TempDir()` 跑單元測試,確認 bash/zsh/fish 各寫到正確路徑

### Phase 2.E — Mock integration

1. `cd tools/leet && go test ./internal/cli/ -run TestInit` → 在 temp dir
   驗證兩種 layout 行為,**完全離線**
2. `go test -count=10` → 不 flaky(mock server 啟動關閉乾淨)

---

## 實作順序

1. `bash bootstrap-project.sh --install-hook`(一次性,無風險)
2. **本 repo 搬遷 A**:`.claude/` → `.agents/` + symlink、`CLAUDE.md` →
   `AGENTS.md` + symlink。獨立 commit,跟程式碼分開,出問題容易回滾。
2a. **本 repo 搬遷 B**:寫 `pyproject.toml`(含 ruff/pytest/coverage 配
    置)、刪 `requirements.txt` + `.coveragerc`、跑 `uv sync` 產 `uv.lock`、
    驗 `uv run pytest` 既有 600+ 題全綠。獨立 commit。
3. `internal/config/` package + tests(無外部依賴,先做)
4. 重構 `internal/categories/` accept config
5. 重構 `internal/scaffold/` accept config + structured templates + meta.go
   (含 kebab / snake / camel converters、strategies + kind schema)
6. 寫 `.leet/config.toml` `layout = "legacy"` 到本 repo
7. 改 `internal/cli/{daily,contest,submit,readme}.go` load config(此時應
   全部既有行為 unchanged)
8. **Smoke**:`leet daily --no-edit` 在本 repo 上跑一次,確認 legacy 行為
   完全不變(這是回歸測試的關鍵點)
9. Mock infra(`mocks_test.go` + `testdata/*.json`)
10. `internal/cli/init.go` + `scaffold/repo_init.go`(structured layout 第
    一次有 caller,含 symlink 建立邏輯)
11. 整合測試覆蓋兩種 layout(temp dir 跑 init → daily → 驗證檔案結構)
12. `internal/leetcode/interpret.go` + `cli/test.go --online`
13. `internal/cli/completion_install.go`(shell completion;cobra 已有 base,只加 install wrapper)
14. `--watch` flag(stretch goal,可砍)

預估 effort:

- bootstrap 跑完:5 分鐘
- 本 repo 搬遷 A+B(symlinks + pyproject.toml):20 分鐘
- config 重構:1 個 evening
- init + structured templates:1 個 evening
- mock infra + 整合測試:1 個 evening
- online test + interpret:1 個 evening
- shell completion install wrapper:30 分鐘
- 總計 ~3-4 個 evening
