# Experiment Log: AutoResearch for Predicting Next-Year Defensive Value in MLB

**Project:** AutoResearch for Predicting Next-Year Defensive Value in MLB  
**Author:** Presley Nevadomsky  
**Research Question:** Can an AI agent discover the best model for predicting an outfielder's OAA next season from their physical tracking data this season?  
**Target Variable:** next_year_oaa (Outs Above Average in year N+1)  
**Input Features:** Year N physical tracking stats (burst, reaction, routing, bootup, sprint speed, age)  
**Validation Metric:** val_rmse (lower is better)  
**Train/val:** 2016-2022 seasons (430 matched pairs)  
**Test:** 2023 → 2024 OAA (69 rows, locked)  
**Baseline:** 4.759972 (all features, linear regression)  
**Current Best:** 4.759972

---

## Experiment-Result Matrix

| # | Date | Description | What Changed | Features | Val RMSE | vs Baseline | Result | Error Type |
|---|------|-------------|--------------|----------|----------|-------------|--------|------------|
| 1 | 2026-05-10 | Baseline: all features linear regression | Starting point | all 7 | 4.759972 | — | baseline | — |

---

## Error Taxonomy

### Signal Failure — *Loop ran but no meaningful improvement*
No instances yet.

### Code Instability — *Crashes or broken pipeline*
No instances yet.

### Agent Misbehavior — *Agent broke the rules or made uncontrolled changes*
No instances yet.

### Evaluation Leakage — *Metric improved but comparability was compromised*
No instances yet.

---

## Key Findings

- **Baseline RMSE:** 4.759972 — predicting next-year OAA is harder than same-year OAA (previous baseline was 4.524665)
- More findings to be added as experiments run