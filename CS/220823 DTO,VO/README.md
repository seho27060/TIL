# Entity, DTO, VO

### Entity

- Java내에서 DB의 테이블에 존재하는 Column들을 필드로 가지는 객체

- Entity는 DB의 테이블과 1대1 대응한다.

- Entity클래스는 다른 클래스를 상속받거나 인터페이스의 구현체여서는 안되고, 순수한 데이터 객체인것이 좋다.

```java
@Entity
@NoArgsConstructor
@AllArgsConstructor
public class Challenge {

    @Id // primary key
    @GeneratedValue(strategy = GenerationType.IDENTITY) // 생성 값에 대한 strategy 할당, 데이터가 생성될 수록 index 증가
    private Long id;

    private String name;

    private int level;

    private String content;

}
```

- `Challenge`라는 Entity 클래스가 형성되었다.

### DTO(Data Transfer Object)

- 계층간 데이터 교환을 위한 객체(Java Beans)
  
  - Client와 Controller간 요청-응답을 보낼 때도 RequestDto의 형식으로 데이터를 보낸다.
  
  - Controller - Service - Repository 계층 사이에 데이터가 오갈때도 역시 DTO의 형태로 이동한다.
  
  - DB에서 데이터를 얻어 Service나 Controller등으로 보낼때 사용하는 객체
  
  - DB의 데이터가 Presentation Logic Tier로 넘어갈때 DTO의 모습으로 변환되어 전송된다.
  
  - 로직을 갖지 않는 순수한 데이터 객체, `getter`, `setter`메서드만을 갖는다. 다만 단순히 데이터를 옮기는 용도이기 때문에 `setter`가 아닌 생성자만으로 값을 할당하는게 좋다.

#### 왜 DTO를 사용할까?

1. View Layer와 DB Layer의 역할을 분리하기 위해

2. Entity 객체의 변경을 피하기 위해

3. View 와 통신하는 DTO 클래스는 자주 변경된다. 따라사 Entity 클래스와 분리하여 관리하는게 좋다.

4. 도메인 모델링을 지키기 위해 - Entity 클래스의 특정 컬럼들을 조합하여 특정 포맷을 출력한다고 할때, Entity 클래스에 직접 접근을 하는 표현을 위한 필드나, 로직이 추가되면 객체 설계가 망가질 수 있다. 따라서 DTO에 표현을 위한 로직을 추가하여 관리하는것이 Entity 도메인 모델링을 지킬 수 있다.

#### VO(Value Object)

- 값 그 자체를 나타내는 객체

- VO는 객체들의 주소가 달라도 값이 같으면 동일한 것으로 여긴다.
  
  - 이를 위한 값 비교를 위해 `equals()`와 `hashcode()`메서드를 오버라이딩 해주도록 한다.

- DTO와 다르게 로직을 포함할 수 있다.

- 특정 값 자체를 표현하기 때문에 불변성의 보장을 위해 생성자를 사용한다.
