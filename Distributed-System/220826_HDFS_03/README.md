- [HDFS\_03](#hdfs_03)
  - [HDFS](#hdfs)
    - [Partitioner Class](#partitioner-class)
      - [Partitioner Class 사용하기](#partitioner-class-사용하기)

# HDFS_03

## HDFS

### Partitioner Class

- Map 함수의 출력인 (KEY,VALUE)쌍이 KEY에 의해서 어느 Reducer로 보내질 것인지 정하는 Class

- 하둡의 기본 타입은 Hash함수가 Default로 제공되며, key에 대한 해시값에 따라 어느 Reducer로 보낼지 결정한다.

#### Partitioner Class 사용하기

- Map함수의 출력인 (key,value)쌍에서 key가 intWritable 타입이고, Value는 Text타입일때, Partioner를 수정하여  key값이 30이하 일때를 구분하여 다른 reducer로 전송하기 위해서는 Partioner class를 수정해야 한다.

```java
public static calss MyPartitioner extends Partitioner<IntWritable, Text>{
    @Override
    public int getPartition(IntWritable key, Text value, int numPartitions){
        int nbOccurences = key.get(); // key의 값 뽑아냄
        if(nbOccurences <= 30) return 0;
        else return 1;
}
}
```

- 위 처럼 Partitioner class를 정의한다.

- Main 함수에 `job.setPartitionerClass(MyPartitioner.class);`를 추가한다.

- Partitioner class 를 import 한다. `import org.apache.hadoop.mapreduce.Partitioner;`


