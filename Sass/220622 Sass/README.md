[toc]
# 220622 TIL
## Sass
### Sass(Syntactically Awesome StyleSheet)

- CSS의 사용에 있어 코드의 재활용성을 올리고, 가독성을 개선하기 위한 CSS 전처리기 언어.
- CSS에서는 없는 nesting, 혼합, 상속, 및 유지 관리에 도움을 주는 기능이 있다.

### Sass Tutorial
#### Variables
- Sass에서는 함수를 선언하고 특정값을 할당하여 재사용이 가능하다.s

```css
$font-stack: Helvetica, sans-serif;
$primary-color: #333;

body {
    font: 100% $font-stack;
    color: $primary-color;
}
```

- body 태그의 font, color에 각 font-stack, primary-color 변수에 저장된 값들이 할당된다.

#### Nesting
- CSS에서의 nesting(중첩)된 구조를 보다 가독성있게 작성 가능하다.

```css
Sass 출력
nav
  ul
    margin: 0
    padding: 0
    list-style: none

  li
    display: inline-block

  a
    display: block
    padding: 6px 12px
    text-decoration: none

CSS  출력
nav ul {
  margin: 0;
  padding: 0;
  list-style: none;
}
nav li {
  display: inline-block;
}
nav a {
  display: block;
  padding: 6px 12px;
  text-decoration: none;
}
```

#### Modules

- @use  를 활용하여 다른 Sass 파일을 module과 같이 load 할 수 있따. 
- filename에 기반하여 해당 파일에 포함된 변수, mixins, 함수를 사용 가능하다.

```css
// _base.sass
$font-stack: Helvetica, sans-serif
$primary-color: #333

body
  font: 100% $font-stack
  color: $primary-color
```

```css
// styles.sass
@use 'base'

.inverse
  background-color: base.$primary-color
  color: white
```

#### Mixins 
- @mixin을 활용하여 사이트 내에서 재사용이 가능한 CSS 선언 그룹을 제작하여 사용할 수 있다. 

```css
@mixin theme($theme: DarkGray)
  background: $theme
  box-shadow: 0 0 1px rgba($theme, .25)
  color: #fff


.info
  @include theme

.alert
  @include theme($theme: DarkRed)

.success
  @include theme($theme: DarkGreen)

```

- @mixin 으로 할당된 theme이 아래 3개의 태그에 재사용되었다.



#### Extend/Inheritance



