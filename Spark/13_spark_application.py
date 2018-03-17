# Python application stub
import sys

from pyspark.sql import SparkSession

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print >> sys.stderr, "Usage: accounts-by-state.py <state-code>"
    sys.exit()
    
  stateCode = sys.argv[1]

  spark = SparkSession.builder.getOrCreate()

  df = spark.read.table("accounts")
  df = df.filter(df.state == stateCode)
  df.write.mode("overwrite").save("/loudacre/accounts_by_state/" + stateCode)

  spark.stop()

