## 객체 지향 프로그래밍

### 객체 지향 프로그래밍의 필요성(feat. 절차 지향 프로그래밍)
- 절차 지향 프로그래밍에서 순서에 따라서 로직을 구축
- 반복되고 유사한 기능의 로직은 하나의 메서드(함수)로 묶어서 코드 관리
- 그럼에도 불구하고 프로그램이 커지면서 코드가 복잡해짐
  - 메서드와 메서드가 사용하는 변수 사이의 (코드)거리가 길어짐 → 메서드가 사용하는 변수가 오염될 수 있는 가능성 커짐
- 객체 지향 프로그래밍의 시작은 비슷한 기능을 하는 **변수(상태)와 행위(메서드)를 묶자**는 아이디어

### 객체 지향 프로그래밍의 주요 개념
1. 추상화
   - 복잡한 현실을 단순하게 SW로 모델화
2. 부품화
   - 거대한 프로그램을 자세히 뜯어보면 부분 집합들의 소통으로 볼 수 있다
3. 은닉화/캡슐화
   - 유사한 기능의 변수와 메서드를 하나의 클래스로 캡슐화하여서 숨김으로써 멤버를 보호한다 
4. 인터페이스
   - 내부의 자세한 구현은 숨기지만 인터페이스를 규격화하여서 소통은 가능하게 만든다

### 객체, 클래스, 인스턴스
1. 객체, 개념
   - 객체는 클래스로부터 만들어진 대상을 총칭하는 용어로서 개념적인 표현이다
   - 객체는 클래스의 인스턴스이다
2. 클래스, 설계도
   - 클래스는 객체를 생성하기 위한 틀이다
3. 인스턴스, 실제 메모리에 있는 구체적인 실체
   - 클래스로부터 객체를 생성하여서 메모리에 올라오면 하나의 인스턴스가 된다

## 클래스와 인스턴스: static의 이해

### static 키워드
- static 키워드 유무로 클래스 멤버와 인스턴스 멤버를 구분한다
  - static 키워드가 필드(클래스에 정의된 변수의 총칭)나 메서드에 붙으면 클래스 변수 혹은 클래스 메서드가 된다
  - static 키워드가 없는 필드나 메서드는 인스턴스 변수 혹은 인스턴스 메서드가 된다

### 클래스 변수/메서드 vs 인스턴스 변수/메서드
- 인스턴스를 생성하면 클래스 변수/메서드와 인스턴스 변수/메서드를 활용할 수 있다
- 인스턴스를 생성하지 않고 인스턴스 변수/메서드를 활용할 수 없다
  - 클래스 변수/메서드에서 인스턴스 변수/메서드를 사용할 수 없다. (Cannot make a static reference to the non-static field)

```java
class StaticClass {
    public static String static_variable = "Static Variable";
    public static void static_method() {
        System.out.println("This it Static Method");
    }
}

class NonStaticClass {
    public String non_static_variable = "Non Static Variable";
    public void non_static_method() {
        System.out.println("This is Non Static Method");
    }
}

public class Main{
    public static void main(String[] args) {
        StaticClass static_class = new StaticClass();
        NonStaticClass non_static_class = new NonStaticClass();

        System.out.println(static_class.static_variable);
        System.out.println(non_static_class.non_static_variable);

        static_class.static_method();
        non_static_class.non_static_method();

        System.out.println(StaticClass.static_variable);
        // System.out.println(NonStaticClass.non_static_variable); // Error

        StaticClass.static_method();
        // NonStaticClass.non_static_method(); // Error
    }
}

```

- 클래스 변수/메서드는 공유되기 때문에 하나의 인스턴스에 클래스 변수를 변경하면 다른 인스턴스의 클래스 변수에도 영향이 간다
```java
class MixedStaticClass {
    public static String static_variable = "Static Variable";
    public String non_static_variable = "Non Static Variable";
}

public class Main{
    public static void main(Sting[] args) {
        MixedStaticClass first_instance = new MixedStaticClass();
        MixedStaticClass second_instance = new MixedStaticClass();

        System.out.println(MixedStaticClass.static_variable);   // Static Variable
        System.out.println(first_instance.static_variable);     // Static Variable
        System.out.println(second_instance.static_variable);    // Static Variable

        first_instance.static_variable = "Static Variable by first";   
        first_instance.non_static_variable = "Non Static Variable by first";   
        
        System.out.println(MixedStaticClass.static_variable);   // Static Variable by first
        System.out.println(first_instance.static_variable);     // Static Variable by first
        System.out.println(second_instance.static_variable);    // Static Variable by first

        System.out.println(first_instance.non_static_variable); // Non Static Variable by first
        System.out.println(second_instance.non_static_variable);// Non Static Variable
    }
}
```

- 대표적인 클래스 메서드로는 main() 함수가 있다. 이는 main() 함수는 JVM에서 인스턴스화 되지 않고 실행된다.


### 클래스 변수/메서드의 필요성(static을 사용하는 이유)
- 모든 인스턴스에서 공유되는 변수라면 클래스 변수로 사용한다
  - 공유되는 변수가 만약 값이 변경되지 않는 경우라면 final 까지 사용해야한다
- 인스턴스화 되지 않고 클래스의 변수와 메서드를 실행하고 싶은 경우
  - 상태 유지가 필요없는 일회성의 메서드를 실행하기 위해서 클래스를 객체화하는 것은 메모리 낭비이다


## 변수를 제대로 사용하기: 유효 범위

### 필드란 무엇인가
- 필드: 클래스에서 사용하는 모든 변수
- 클래스에서 사용하는 변수는 클래스 변수(static), 인스턴스 변수, 지역 변수가 있다
  - 인스턴스 변수가 사실상 전역 변수이다. (클래스의 메서드에서 전역으로 사용되는 변수)

### 전역 변수는 죄악인가?
- 절차 지향 언어에서 전역 변수는 죄악이다
  - 전역 변수로 선언한 변수를 프로그램 과정에서 잘못 건드리면 코드의 유지 보수가 어렵다
- 하지만 객체 지향 언어에서 전역 변수는 합리적으로 사용할 수 있다
  - 절차 지향 언어에서 객체 지향 언어로 이전하면서 로직(메서드) 뿐만이 아니라 로직을 위한 전용 변수(변수)까지도 하나의 클래스로 묶였다
  - 따라서 전역 변수는 유사한 기능의 메서드들 사이에서 '전역'이기 때문에 합리적으로 사용할 수 있다

### this 키워드
- 변수의 우선 순위는 지역 변수 → 전역 변수이다
- 따라서 지역 변수와 전역 변수의 이름이 동일하다면 지역 변수를 의미한다
- 만약 전역 변수를 가리키고 싶다면 this 키워드를 사용한다
- this 키워드의 의미는 '이 객체(인스턴스)의 것'을 의미한다
  - this는 인스턴스가 생겼다고 가정하고 해당 인스턴스 소유를 의미한다
  - 따라서 클래스 메서드(static method) 내부에서는 this로 변수를 가리킬 수 없다

```java
class ScopeClass {
    int i = 10;
    private void _iterate() {
        for (this.i = 0; this.i < 10; this.i++) {
            System.out.println(this.i);
        }
    }
    public static void static_iterate(int i){
        // this.i = i;          // Error
        // this._iterate();     // Error
    }
    public void non_static_iterate(int i) {
        this.i = i;
        this._iterate();
    }
}
```

## 상속

### 상속의 필요성
- 기존의 클래스에 새로운 메서드를 추가하기 어려운 경우 우리는 상속을 통해 새로운 기능을 수정해야한다
- 기존의 것을 상황에 맞게 활용하기 위해서는 상속이 불가피하다
- 따라서 상속의 핵심은 원래의 클래스(부모 클래스, 상위 클래스)를 변경하지 않는 것이다.

### 상속을 통한 장점
- 코드의 재활용성: 부모 클래스를 매번 코딩할 필요 없이 상속을 통해 기능을 사용
- 코드의 유지 보수: 부모 클래스를 변경하면(권장하지 않지만) 이에 맞게 자식 클래스가 일괄 변경됨
  - 부모 클래스 + 자식 클래스를 하나의 클래스로 하였다면 일일이 잘못된 부분을 찾아서 고쳐야한다

### 상속 관계의 인스턴스를 생성하기: 생성자
- 생성자는 클래스를 객체화 할 때에 호출되는 것으로 인스턴스가 생성될 때 반드시 수행하는 로직을 구현한다
- 상속 관계에서는 자식의 생성자가 먼저 호출되고 부모의 생성자가 호출된다
  - 이 때 super 키워드를 사용해서 부모의 인스턴스를 가리키도록 할 수 있다.
- 부모 클래스의 생성자 처리가 완료되어야 자식 클래스의 인스턴스가 생성될 수 있다
  - 호출은 자식에서 부모이지만 부모에서 필요한 처리가 완료되어야 자식에서 필요한 처리를 연달아 수행

```java
class ParentClass {
    public ParentClass() {
        System.out.println("ParentClass Constructor Start");
        System.out.println("ParentClass Constructor End");
    }
}

class ChildClass extends ParentClass {
    public ChildClass() {
        super();    // designate which constructor of super class to be used: use default constructor
        System.out.println("ChildClass Constructor Start");
        // super(); // Error
        System.out.println("ChildClass Constructor End");
    }
}

public class Main {
    public static void main(String[] args) {
        ChildClass child = new ChildClass();
        /*
        ParentClass Constructor Start
        ParentClass Constructor End
        ChildClass Constructor Start
        ChildClass Constructor End
        */
    }
}
```

### 상속의 의미: 오버로딩과 오버라이딩
1. 오버로딩: 동일한 메서드 명 + 리턴 타입이지만, 매개 변수의 갯수와 타입이 다른 로직을 수행
2. 로버라이딩: 상속 관계에서 부모의 메서드를 자식이 재정의해서 수행
   - 자식의 상황에 맞게 부모의 기능을 수정한다는 점에서 상속의 의미를 담고 있는 전략

## 복잡해진 객체 사이의 관계: 접근 제어자

### 접근 제어자의 필요성
- 이름의 충돌을 방지하기 위해서 접근할 수 있는 범위를 지정한다
- 자바는 패키지라는 상위의 그룹 단위가 있으므로 이를 고려한 접근 제어자의 범위를 정했다

### 접근 제어자 사용 방법
- 접근 제어자를 의미하는 public, protected, default, private를 변수, 메서드, 클래스 앞에 붙이다

### 접근 제어자의 범위
||같은 클래스|같은 패키지 + 상속 관계|다른 패키지 + 상속 관계|다른 패키지|
|-|-------|------------------|------------------|--------|
|public|접근 가능|접근 가능|접근 가능|접근 가능|
|protected|접근 가능|접근 가능|접근 가능|접근 불가능|
|default|접근 가능|접근 가능|접근 불가능|접근 불가능|
|private|접근 가능|접근 불가능|접근 불가능|접근 불가능|

### 클래스와 접근 제어자
- 하나의 파일에는 하나의 public 클래스만 있어야한다
  - 따라서 파일의 이름은 public 클래스의 이름을 따른다


## 객제 지향성의 꽃: 다향성 (feat. 추상클래스, 인터페이스)

### 추상 클래스의 필요성
- 공통된 사항은 일반적인 메서드로 구현한다
- 상황에 따라서 구체적인 수행 방법이 다른 경우 해당 기능 구현 자체는 강제하되 구체적인 구현 방법은 자유롭게 한다
- 추상 클래스는 일반적인 메서드와 추상 메서드로 혼용하여서 공통적인 로직은 일반적인 메스드로 구현하고 상황에 따른 특수한 로직은 추상 메서드로 구현하여서 자식 클래스에서 반드시 구현하도록 제어한다

### 추상 클래스
- 추상 클래스는 추상 메서드를 가지고 있는 클래스있거나 abstract 키워드가 붙은 클래스이다
- 추상 메서드는 로직을 구현하지 않는다
  - 추상 메서드는 자식 클래스에서 오버라이딩되어서 구현된다

### 인터페이스의 필요성
- 인터페이스의 의미는 통일화된 소통 방식(접근 창구)이다
- 내부 구현은 신경쓰지 않고 대신에 접근 방법에만 통일시켜서 사용할 수 있도록 하는 것이 인터페이스의 목적이다
- 따라서 인터페이스를 상속받은 클래스는 인터페이스가 요구하는 접근 창구를 반드시 구현함으로써 기대를 충족해야한다
- 특히 개발 환경에서 서로 영향을 주는 서비스를 독립적으로 개발하는데, 각자 상대방의 서비스로부터 기대하는 바가 다르다면 통합시키기 어려워진다
- 인터페이스는 통합을 위해서 서로 합의된 규칙을 강제하기 위해서 필요하다

### 인터페이스
- 인터페이스의 변수는 static final 변수이고, 인터페이스의 메서드는 추상 메서드이다
- 인터페이스의 접근 제어자는 반드시 public이다.
- 클래스는 다수의 인터페이스를 상속받아서 기능을 구현할 수 있다

### 클래스 수준의 다형성
- 동일한 클래스이지만 다른 기능을 수행한다
- 부모 클래스를 데이터 타입으로 하되 실제 인스턴스는 자식 클래스에서 생성한다
  - 자식 클레스에만 있는 메서드: 사용 불가
  - 부모 클래스에만 있는 메서드: 사용 가능 (부모의 로직을 따름)
  - 자식 클래스와 부모 클래스에 있는 메서드: 사용 가능 (오버라이딩, 자식의 로직을 따름)
- 결론적으로 동일한 데이터 타입이지만 다른 기능을 하는 다형성 조건의 클래스가 생성된다

### 인터페이스 수준의 다형성
- 인터페이스는 다중 상속이 가능하다
- 하지만 모든 인터페이스의 기능이 필요한 것은 아니다
  - 비교가 중심인 상황에서는 비교 인터페이스(Comparable)의 로직만 필요하다
- 그렇다면 인터페이스를 데이터 타입으로 하여서 구현 클래스를 생성한다
  - 구현 클래스에만 있는 메서드: 사용 불가
  - 인터페이스에 있는 메서드: 사용 가능 (구현 클래스에 정한 로직을 따라서 실행)
- 따라서 다른 인터페이스의 기능을 신경쓰지 않고 순간에 집중할 수 있다.