CREATE OR REPLACE TABLE transactions AS SELECT * FROM read_csv_auto('./data/raw/train_transaction.csv');
CREATE OR REPLACE TABLE identity AS SELECT * FROM read_csv_auto('./data/raw/train_identity.csv');

 -- 75% of transactions don't have identity info
 -- so the choice of left join as to preserve the data
CREATE OR REPLACE VIEW fraud_transactions AS (
    SELECT * 
    FROM transactions
    LEFT JOIN identity
    ON transactions.TransactionID = identity.TransactionID
);