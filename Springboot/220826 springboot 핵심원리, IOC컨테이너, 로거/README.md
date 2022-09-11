# Springboot_04

## Spring 핵심원리

### 객체 지향 설계 5가지 원칙 - SOLID

#### SRP(Single Responsibil) : 단일 책임 원칙

- **한 부품**(클래스, 메서드)는 **하나의 책임**만 지닌다.

- 하나의 기능이 변경될때, 해당 역할을 지니는 클래스만 변경되어야 한다.

- 클래스 내부에서 함수끼리 강한 결합도를 가지면 유지보수에 많은 비용이 들게 되므로, 역할에 따라 책임을 분리한다.

#### OCP(Open/Closed Principle) : 개방-폐쇄 원칙

- 확장에는 열려있으나, 변경에는 닫혀있어야 한다.

- 하나의 기능을 추가할때, 기존 코드는 변경(Closed)없이 기능을 수정하거나 추가(Open)할 수 있도록 만들어야 한다.

- 클래스, 메서드 단위별로 추가되어도 기존 코드와의 결합은 없어야 한다.

#### LSP(Liskov Substitution Principle) : 리스코프 치환 원칙

- 리스코프가 제안한 원칙

- 객체지향 프로그래밍에서는 부모, 자식 인스턴스를 치환해도 문제가 없어야 한다.

- 상속관계에서는 **일반화 관계**(IS-A)가 형성되어야 한다. 즉 일관성이 존재한다.

- 일반화 관계 : 여러 개체들이 가진 공통된 특성을 부각시켜 하나의 개념이나 법칙으로 성립시키는 과정

#### ISP(Interface Segregation Principle) : 인터페이스 분리 원칙

- 한 클래스는 자신이 사용하지 않는 인터페이스는 구현하지 말아야 한다.(클래스 자신이 사용하지 않는 기능(인터페이스)에는 영향을 받지 말아야 한다.)

- **인터페이스 분리**를 통해 시스템 **내부 의존성을 약화**시켜 리팩토링, 수정, 재배포를 쉽게 할 수 있다.

#### DIP(Dependency Inversion Principle) : 의존관계 역전 원칙

- 의존 관계를 맺을때, 변화하기 쉬운것 보단 변화하기 어려운것에 의존해야 한다.

- 변화하기 쉬운 것 = 구체적인 것(구체화된 클래스), 변화하기 어려운 것 = 추상적인것(추상 클래스, 인터페이스)

- 즉, DIP를 만족하는 것은 상속에 있어서 구체적인 클래스보다, **인터페이스나 추상 클래스**와 관계를 맺는다는 의미이다.

### 스프링 IOC 컨테이너

- 스프링에서 OCP를 지키다보면, DIP에 어긋나는 흐름이 있다. 이러한 경우를 위한 **DI(Dependency Injection, 의존성 주입)** 컨테이너와 **IoC(Inversion of Control)** 를 통해 해결한다.

- `ApplicationContext`라고 하며, 어노테이션을 통해 Bean을 인지하면 해당 컨테이너(Context)에 등록한다.

- `ApplicationContext`은 `BeanFactory`라는 최상위 인터페이스를 상속받아 기능을 제공한다. 상속으로 기본기능을 사용하며, `ApplicationContext`에서 추가기능을 구현하여 제공한다. 

#### DI(Dependency Injection, 의존성 주입)

- 의존성 : 클래스간에 관계에 따라 하나의 클래스 객체 내에서 다른 클래스가 연관된 상태. 의존성이 강하면 클래스간의 결합도가 높아지고, 이는 유지보수에 곤란하게 된다.

- 과한 의존성을 억제하기 위해 스프링에서는 의존성 주입(DI)를 통해 모듈간의 결합도를 낮춘다.

- 의존성 주입(DI,Dependency Injection) : IoC Container가 개발자 대신 xml파일에 정의한대로 Bean 객체를 생성하고 의존성을 대신 주입하는것을 의미한다.(IoC, 제어의 역전 발생)

#### IoC(Inversion of Control, 제어의 역전)

- 객체가 함께 동작해야하는 의존성을 정의하는 처리 과정

- 클래스 객체와 다른 클래스 객체가 연관될때(의존성), 기존에는 사용자가 직접 연관관계를 명시해줘야 했다.

- 스프링에서는 IoC컨테이너를 통해 그 행위를 대신한다.

- 사용자가 직접 관계를 제어하는 권한을 스프링에 위임하여, 스프링이 대신 관계 제어를 하므로 이를 제어의 역전 이라고 한다.

#### Bean

- Spring에 의하여 생성되고 관리되는 자바 객체
- 아래에 `@Component`, `@Bean`두개의 어노테이션을 통해 컨테이너에 등록할 수 있다.
- 등록시에 Bean id로 클래스, 메서드의 이름이 디폴트로 카멜케이스로 등록된다.
- 작성자가 임의로 Bean id를 수정하여 할당할 수 도 있다.

#### 컨테이너 관련 어노테이션

##### @Configuration

- 구성 정보를 담당하는 클래스를 설정할때 사용한다.
- 해당 어노테이션이 할당된 클래스 내에서 메서드에 대해 빈 등록을 마치면, Context에 저장하게 된다.
- 이후 App 파일에서 해당 어노테이션이 할당된 BeanFactory의 종류중 하나인AnnotationConfigApplicationContext의 객체를 불러와 사용을 명시한다.

```java
ApplicationContext factory = 
    new AnnotationConfigApplicationContext(클래스명.class); 

BeanClass scanBean = factory.getBean("beanClass", BeanClass.class);
```

##### @ComponentScan

- Spring에서 컴포넌트를 인식하는 어노테이션으로, 해당 클래스내에서 `@Component`, `@Service`, `@Repository`, `@Controller`, `@Configuration`로 등록된 하위 클래스를 1개라도 찾으면, Context에 Bean으로 등록한다.

##### @Component

- 개발자가 생성한 Class를 Spring의 Bean으로 등록할 때 사용한다.(직접 제어 가능)

- 등록된 Bean은 **싱글톤**으로 관리된다. `@Scope`어노테이션을 통해 타입을 수정하여 싱글톤이 아닌 빈도 생성가능하다.

- Spring에서는 `@ComponentScan`을 통해 해당 어노테이션을 등록대상으로 인지한다.

- 작성자가 커스터마이징이 가능한 클래스

##### @Bean

- 개발자가 제어가 불가능한 외부 라이브러리와 같은 것들을 Bean으로 등록한다.(직접 제어 불가능)

- 주로 `@Configuration`어노테이션이 할당된 Spring을 설정하는 클래스 내에 들어가는 메서드에 선언한다.

- 해당 클래스는 스프링에 등록된다.

##### @Autowired

- Bean 객체간의 의존성 주입을 위해 Configuration을 통해 일일히 설정해줘야 했으나, `@Autowired`어노테이션을 통해 자동으로 주입이 가능하다.

- Component 내에서 `@Autowired`가 붙은 객체를 인지하면 Spring에서는 Spring Container에 저장된 Bean 목록중에서 매칭되는 Bean객체를 찾아 의존성을 주입해준다.

- Spring은 Class를 보고 Type에 맞게 Bean을 주입한다.

###### 다양한 의존관계 주입 방법

1. 생성자 주입 : 제일 범용적인 방식
   
   ```java
   @Component
   public class OrderServiceImpl implements OrderService{
   private final MemberRepository memberRepository;
   private final DiscountPolicy discountPolicy;
   @Autowired
   public OrderServiceImpl(MemberRepository memberRepository,DiscountPolicy discountPolicy){
       this.memberRepository = memberRepository;
       this.discountPolicy = discountPolicy;
   }
   ...
   }
   ```

2. 수정자 주입

3. 필드 주입

4. 일반 메서드 주입
- 위 방법들로 의존성 주입이 가능하나 **Lombok**라이브러리를 통해 간단하게도 가능하다.

##### @RequiredArgsConstructor

- Lombok라이브러리에서 제공하는 어노테이션으로, final이 붙은 필드에 대한 생성자를 자동으로 만들어준다.

```java
@Component
@RequiredArgsConstructor
public class OrderServiceImpl implements OrderService {
    private final MemberRepository memberRepository;
    private final DiscountPolicy discountPolicy;
}
```

- 위 예시는 "다양한 의존관계 주입"에서의 예시코드와 같은 내용이다. 다만 `@RequiredArgsConstructor`를 통해 코드가 더욱 간단하게 구현되었다.

- 코드의 간결화에 의해 `@Autowired`를 지양하고, `@RequiredArgsConstructor`를 사용하여 한번에 처리하는게 최신 트렌드라고 한다.

## Logger

- log(시간, 패키지의 위치, 메서드 명)를 남겨주는 클래스

- Logger가 없다면 디버깅시에 `println`을 통해 콘솔에 출력하여 확인해야 하나, 애플리케이션의 사이즈가 커지면 이는 상당히 곤란하게 된다.

- `slf4j`에서 `Logger`를 사용하도록 한다.

- `private final Logger logger = LoggerFactory.getLogger(SomeServiceImpl.class);` 를 통해 **Controller**내에 logger 생성

- 로그정보를 확인할려는 `Contoller`에 매핑된 함수 내에서 아래와 같이 사용한다.

```java
@GetMapping("/read")
public void exampleMethod{
    ...
    logger.로그레벨("로그메세지");
    ...
}
```

#### 5단계의 로그 레벨(1:상위 - 5:하위)

- 심각한 정도에 따라 아래 5개 레벨로 분류한다.
  
  1. Error : 예상치 못한 심각한 문제가 발생하는 경우, 즉시 조취 필요
  
  2. Warn : 로직 상 유효성 확인, 예상 가능한 문제로 당장 서비스 운영에 영향은 없지만, 주의해야 한다.
  
  3. Info : 운영에 참고할만한 사항, 중요한 비즈니스 프로세스가 완료됨
  
  4. Debug : 개발 단계에서 사용하는 메시지
  
  5. Trace : 모든 레벨에 대한 로깅, DEBUG보다 상세한 로깅 정보 출력

- 실행흐름에서 원하는 단계의 정보만 선택적으로 확인할 수 있다.

- 지정한 레벨보다 낮은 레벨의 메시지들은 출력되지 않으나, 높은 레벨은 출력한다.
