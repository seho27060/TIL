# HDFS_01

## HDFS

### index1

### Linux와 HDFS

![](C:\Users\161548\AppData\Roaming\marktext\images\2022-08-25-14-28-44-image.png)

- 데이터 생성이나 코딩은 Linux에서 하고 MapReduce 코드와 입력 데이터는 HDFS에 옮겨서 MapReduce 알고리즘을 수행한다.

### Word Count MapReduce 예제 코드

```
$cd /home/Project/src
```

- src 형태
  
  - Driver.java
  
  - Wordcount.java

- Wordcount.java를 실행시키기 위해 Driver.java에 추가해줘야함.

```java
package ssafy;

import org.apache.hadoop.util.ProgramDriver;

public class Driver {
    public static void main(String[] args) {
        int exitCode = -1;
        ProgramDriver pgd = new ProgramDriver();
        try {

            pgd.addClass("wordcount", Wordcount.class, "A map/reduce program that performs word cou                    nting.");
// 실행할 코드를 추가해줬다.
                  pgd.driver(args);
            exitCode = 0;
        }
        catch(Throwable e) {
            e.printStackTrace();
        }

        System.exit(exitCode);
    }
}
```

- 실행할 코드를 `addClass`를 사용하여 추가해주고, 터미널상에서 `ant`를 통해 다시 빌드해줘야 한다.
  
  - addClass("program name", class name, "description") 와 같이 작성하면 된다.

- `ant` : JAva 개발환경에서의 표준 빌드 도구

- javac를 사용해도되지만, 여러 종속성을 고려하여 소스파일을 컴파일한다.

- build.xml에 정의한 내용대로 수행된다.

- 실행 코드를 추가하고, 테스트 데이터를 추가한 후.

```
$hadoop jar ssafy.jar wordcount wordcount_test wordcount_test_out
// $ hadoop jar [jar file] [program name] <input arguments...>
```

- 위 코드를 터미널 상에서 실행하여 코드를 수행한다.

#### 맵리듀스 입출력에 사용가능한 디폴트(default) 클래스

- 맵리듀스 프레임워크에서는 키-밸류 를 통해 정렬하므로, 기존의 타입을 사용하지 못하고, 프레임워크에서의 사용에 적합한 타입이 재정의 되어있다.
  
  - 하둡의 맵리듀스의 맵함수, 리듀스 함수, 컴바인 함수 등 입출력에 사용할 수 있는 클래스에 해당하는 자바 타입
    
    - Text : string
    
    - intWritable: int
    
    - LongWritable : long
    
    - FloatWritable : float
    
    - DoubleWritable : double

- 새로운 클래스를 정의해서 입출력에 사용한다면, 위 타입을 사용하여 정의해야 한다.

#### Wordcount.java - Map

![](C:\Users\161548\AppData\Roaming\marktext\images\2022-08-25-15-10-55-image.png)

#### Wordcount.java - Reduce

![](C:\Users\161548\AppData\Roaming\marktext\images\2022-08-25-15-13-26-image.png)

#### Wordcount.java - Main

![](C:\Users\161548\AppData\Roaming\marktext\images\2022-08-25-15-16-57-image.png)

#### Wordcount.java - Main(with Combiner)

![](C:\Users\161548\AppData\Roaming\marktext\images\2022-08-25-15-21-00-image.png)

#### Wordcount.java 를 수정한 다음 실행

- Project 디렉토리에서 ant 수행

- 수행결과 보기
  
  - `$hdfs dfs -rm -r classname_test_out`와 같이 리듀스 함수 출력 디렉토리를 삭제
  
  - `$hadoop jar ssafy.jar classname classname_test classname_test_out` 수정사항을 반영할 클래스로 결과 출력
  
  - `$hdfs dfs -cat classname_test_out/part-r-0000|more`로 사용한 reducer 갯수 만큼 출력결과를 확인한다.

#### Main 함수에서 Mapper나 Reducer에 값을 Broadcast
