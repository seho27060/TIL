[TOC]

# Github Actions

## Github Actions

> GitHub Actions는 빌드, 테스트 및 배포 파이프라인을 자동화할 수 있는 지속적 통합 및 지속적 배포(CI/CD) 플랫폼입니다. 리포지토리에 대한 모든 풀 요청을 빌드 및 테스트하는 워크플로를 생성하거나 병합된 풀 요청을 프로덕션에 배포할 수 있습니다. - Github Docs

- `Jenkins`, `Travis CI`와 같은 툴과 같이 빌드, 테스트, 배포의 작업을 자동화하는 툴이다.

- `Github`에서 자체적으로 제공하는 기능으로 이벤트(`event`)를 발생 시 사전에 설정한 작업(`Job`)를 실행하여 작업 흐름(`workflows`)를 관리할 수 있다.

- `Github Actions`의 기본이 되는 핵심 구성 요소를 알아보자.

### 구성 요소

#### Workflows

> 풀 요청이 열리거나 문제가 생성되는 등 리포지토리에서 *이벤트가* 발생할 때 트리거되도록 GitHub Actions *워크플로를 구성할 수 있습니다.* - Github Docs

- `Github Actions`가 특정 `events`를 감지했을 경우 실행하는 `jobs`를 실행하는 집합

- `jobs` 간에 관계를 형성하여 순차적으로 작업을 진행하거나. 특정 `event`에 따라 정해진 작업을 **자동**으로 수행할 수 있다.

- `repository` 내에서 `.github/workflows` 폴더 아래에 위치한 `YAML` 파일 설정을 통해 `workflows`를 생성할 수 있다.
  
  - 특정 `branch`에서 특정 `event`가 발생했을 시, 특정 `jobs`을 실행하도록 설정한다.

#### Events

> 이벤트는 워크플로 실행을 트리거하는 리포지토리의 특정 활동입니다. - Github Docs

- `push`, `pull` 과 같은 `repository`에 영향을 주는 활동을 의미한다.

- `event`가 감지되었을 경우 설정에서 따라  `workflows` 트리거(`trigger`)한다.

#### Jobs

> 작업은 동일한 실행기에서 실행되는 워크플로우의 *일련 의 단계(`step`입)니다.* 각 단계는 실행될 쉘 스크립트이거나 실행될 *조치(`actions` )입니다.* 단계는 순서대로 실행되며 서로 의존적입니다. - Github Docs

- `Jobs`는 여러개의 `step`로 구성되어 있다.
  
  - `step`는 기본적으로 병렬적으로 실행되나, 서로간에 의존 관계를 설정할 수 있다.

- 각 `Step`는 `Runner`라는 가상 머신에 의해 실행되어 `Step`간에 데이터를 공유할 수 있다.

#### Actions

> `Actions`*는* 복잡하지만 자주 반복되는 task를 수행하는 GitHub Actions 플랫폼용 사용자 지정 애플리케이션입니다. - Github Docs

- `Actions`를 통해 `workflows` 파일을 작성하는 반복 코드의 양을 줄이는 데 도움이 된다.

- `Actions`에 task를 공유하여 동일 `repository`에서 사용하거나 `public` `repository`에 공유하여 `Github`상의 모든 `repository`에 공유할 수 있다.
  
  - [GitHub Marketplace](https://github.com/marketplace?type=actions)에서 다양한 공개 `Actions`를 사용할 수 있다.

#### Runners

> `Runners`는 트리거될 때 `Workflows`를 실행하는 서버입니다. 각 `Runners`는 한 번에 하나의 `Job`을 실행할 수 있습니다.

- `Ubuntu Linux`, `Microsoft Windows`, `macOS` 등의 `OS`를 제공한다.

---

- 레퍼런스

> [Understanding GitHub Actions - GitHub Docs](https://docs.github.com/ko/actions/learn-github-actions/understanding-github-actions)
> 
> https://www.daleseo.com/github-actions-basics/ 
