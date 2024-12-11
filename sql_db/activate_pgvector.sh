#!/bin/bash
set -e

echo "Activating pgvector extension..."

# Activate the pgvector extension
psql -v ON_ERROR_STOP=1 --username "postgres" --dbname "HCSinsurance" <<-EOSQL
  CREATE EXTENSION IF NOT EXISTS vector;
EOSQL

echo "pgvector extension activated successfully."