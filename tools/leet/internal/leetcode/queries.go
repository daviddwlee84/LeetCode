package leetcode

// GraphQL query strings, kept as raw const so they're easy to copy-paste into
// the LeetCode GraphQL Explorer when iterating.

const queryDailyChallenge = `query questionOfToday {
  activeDailyCodingChallengeQuestion {
    date
    link
    question {
      questionId
      questionFrontendId
      title
      titleSlug
      content
      difficulty
      exampleTestcases
      codeSnippets { lang langSlug code }
      topicTags { name slug }
    }
  }
}`

const queryQuestionData = `query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    questionFrontendId
    title
    titleSlug
    content
    difficulty
    exampleTestcases
    codeSnippets { lang langSlug code }
    topicTags { name slug }
  }
}`

const queryUserStatus = `query globalData {
  userStatus { isSignedIn username }
}`

// queryQuestionTitleByID is used by `leet submit` — we have the problem
// number from the filename but need the slug to POST to /problems/{slug}/submit/.
const queryQuestionTitleByID = `query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
  problemsetQuestionList: questionList(
    categorySlug: $categorySlug
    limit: $limit
    skip: $skip
    filters: $filters
  ) {
    questions: data { titleSlug questionFrontendId }
  }
}`
