# Cloudera Spark & Hadoop Developer

* 3/12 - 3/15
* 15名くらい

# Sparkの構成

* Spark Core
  * RDDを使って書く。
  * 非構造データを扱う場合など。
* 高機能のAPI
  * SQL
    * SQLに限らず構造データを扱うAPI
  * Streaming
    * not realtime, マイクロバッチ
    * 最低500msはかかる、数秒単位で処理する
    * Spark Core=RDDベース
    * socketTextStreamは改行まででデータを切る。次の回に回す。
  * MLlib
    * MLlibはDataFrameベース(ml)とRDDベース(mllib)がある
  * GraphX
  * SparkR
    * SparkryRというApacheじゃない実装もある。R使いはこっちの方がいいかも。

# Spark SQL

SQLというより構造データを読み込むためのライブラリ。CSVやJSONを読み込むことができる。

* データソースとして使えるもの。
  * CSV,JSON,RDB(JDBC,ODBC),Hive,Parquetなど。
* アクセスするためのAPIはSQL系とDataFrame/Dataset系の2パターン
  * SQLはAPIを通してSQL文をそのまま文字列として投げ込むもの。
    * ```spark.sql("SELECT first_name, last_name FROM accounts")```
  * DataFrame/DatasetはPython/Scalaのメソッドで操作するもの。
    * ```df.select("first_name","last_name")```
* DataFrame/Datasetの違いは静的型付けかどうか。
  * Javaでいう```List```と```List<T>```の違い。
  * Python,Rは静的型付けじゃないのでDataFrameのみ
  * Scalaはどちらも使えるがDatasetを使うべき
    * Javaで```List<T>```を使う理由と同じ。
    * ScalaのDataFrameは```Dataset<Row>```のalias
  * https://databricks.com/blog/2016/07/14/a-tale-of-three-apache-spark-apis-rdds-dataframes-and-datasets.html
* 実際の動作はSpark CoreのRDDと同じ。
  * Catalyst Optimizerが実行計画を最適化してくれる。
    * map reduceをうまく考えてくれる。

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

# Application

* sparklauncher
* livy REST API

# Streaming

* time slicing
  * Dstream.slice()
  * StreamingContext.remember()
  * これを使うならKafka使った方がいい。
* updateStateByKey
  * 累積
  * checkpointを書く必要がある(ないと実行時エラー)
    * 適宜HDFSにflushされる
  * Expanding Window
* SlidingWindow
  * バッチ間隔と別のタイミングで実行する
  * 過去どれくらいの期間を処理するかwindow幅を指定する。
  * checkpointを書く必要がる。
  * Moving Window
* Structured Streaming
  * Spark 2.3.0で正式リリースされた。
  * RDDではなくDataFrameベース = Optimizerで最適化される
* Kafka + Spark Streming
  * RecieverベースとDirectがありDirectが後発だが推奨
  * DirectはKafkaのtopicのpartitionとSpark RDDのpartitionを一致させる
    * exactly-onceが実現できる(確実に1回だけ実行)
    * 損失ゼロを効率的に実現できる(ReceiverだとWALが必要だった)

# Why Spark

* MLとかになるとTensorflowとか
  * ETLとかMLだけをやる訳ではないのでSparkがいるのでは(川崎さん)
* インフラの堅牢性？
