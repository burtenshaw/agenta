export enum EvaluationFlow {
    EVALUATION_STARTED = "EVALUATION_STARTED",
    COMPARISON_RUN_STARTED = "COMPARISON_RUN_STARTED",
    EVALUATION_FINISHED = "EVALUATION_FINISHED",
}

export enum EvaluationType {
    human_a_b_testing = "human_a_b_testing",
    human_scoring = "human_scoring",
    auto_exact_match = "auto_exact_match",
    auto_ai_critique = "auto_ai_critique",
}
