# Cloudera Spark & Hadoop Developer

* 3/12 - 3/15
* 15名くらい

# Spark SQL

SQLと言うより構造データを読み込むためのライブラリ。CSVやJSONを読み込むことができる。

HDFS上のJSONを読み込む。
(pyspark>はpysparkを立ち上げたコンソールで)

```console
$ hdfs dfs -put devices.json
```

```python
In [11]: df = spark.read.json("/loudacre/devices.json")
                                                                                
In [12]: df.printSchema()
root
 |-- dev_type: string (nullable = true)
 |-- devnum: long (nullable = true)
 |-- make: string (nullable = true)
 |-- model: string (nullable = true)
 |-- release_dt: string (nullable = true)


In [13]: df.show(5)
+--------+------+--------+-----+--------------------+
|dev_type|devnum|    make|model|          release_dt|
+--------+------+--------+-----+--------------------+
|   phone|     1|Sorrento| F00L|2008-10-21T00:00:...|
|   phone|     2| Titanic| 2100|2010-04-19T00:00:...|
|   phone|     3|  MeeToo|  3.0|2011-02-18T00:00:...|
|   phone|     4|  MeeToo|  3.1|2011-09-21T00:00:...|
|   phone|     5|  iFruit|    1|2008-10-21T00:00:...|
+--------+------+--------+-----+--------------------+
only showing top 5 rows
```

# 分散

* shuffleの前に必ずdiskにcacheされる
  * 再利用できるjobでは前のステージがskippedになる
* excecutorは動的割り当て、リソースがあれば1ホストに複数上がる
  * Application Masterもリソースをとるので注意
