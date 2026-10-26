# CI Build Log Analysis

- **Failed test:** `test_adds_processing_fee_once`
- **Failure location:** `test_payments.py:10`
- **Probable cause:** The processing fee appears to have been added twice. For amount 100.00 and fee 8.00, expected 108.00, but the failing run returned 116.00.
- **Recommended check:** Compare the payment total calculation with the requirement to include the processing fee exactly once.
