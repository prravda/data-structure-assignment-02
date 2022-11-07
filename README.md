# Data structure - second assignment

---

# Author
201603001 전인섭

---

# Description
```shell
├── README.md # 전체적인 프로젝트를 설명하는 문서
├── __init__.py
├── mock_tree_dataset.py # test 를 위한 tree 를 구현한 dataset
├── node.py # linked structure 로 tree 를 만들기 위한 기초 자료형 Node
├── test # python 의 unittest module 을 통해 구현한 test
│   ├── __init__.py 
│   ├── test_traverse # tree 순회와 관련된 test
│   │   ├── test_traverser_set_one.py
│   │   └── test_traverser_set_two.py
│   └── test_utilities # tree 의 속성을 계산하는 utility 와 관련된 test
│       ├── test_utilities_set_one.py
│       └── test_utilities_set_two.py
├── traverser.py # tree 순회를 구현한 코드
├── utilities.py # tree 의 속성을 계산하는 기능들을 구현한 코드
└── output_in_console.py # 교재에 기재된 양식으로 console 에 결과물을 출력하는 코드
```

---

# Analysis

## traverse
### preorder
- description: 
  - linked structure 의 tree 가 있을 때, value-left-right 순서대로 탐색을 진행하는 방식을 의미한다.
  - 현재 방문한 node 를 우선 연산처리하고, 그 자식노드들의 연산을 나중에 처리하는 경우에 사용하면 적절하다.
- time complexity: `O(N)`
- reason: 모든 tree 의 node 에 대해서 1번씩의 연산을 하기 때문에, n개의 node 로 이뤄진 tree 가 입력된다면 time complexity 는 `O(N)` 이 된다.
### inorder
- description: 
  - linked structure 의 tree 가 있을 때, left-right-value 순서대로 탐색을 진행하는 방식을 의미한다.
  - terminal node 중 leftmost 한 node 부터 먼저 처리해야 할 때 해당 방식을 사용한다.
- time complexity: `O(N)`
- reason: 상술한 것과 같다.
### postorder
- description: 
  - linked structure 의 tree 가 있을 때, left-right-value 순서대로 탐색을 진행하는 방식을 의미한다.
  - 현재 방문한 node 를 그것의 자식 node 를 처리한 뒤 처리하는 경우에 사용하면 적절하다.
- time complexity: `O(N)`
- reason: 상술한 것과 같다.
### level-order
- description: 
  - linked structure 의 tree 가 있을 때, tree 의 level 순으로 탐색을 진행하는 방식을 의미한다.
  - breadth-first search, BFS(너비우선탐색) 이라는 이름으로도 많이 불리는 탐색법이다.
  - recursive 한 방법으로도 구현할 수 있지만, `FIFO` 성질의 `queue` data structure 를 사용하는 것이 일반적이다. 
- time complexity: `O(N)`
- reason: 상술한 것과 같다.

## utilities
### get number of total nodes
- description: recursive 한 방법으로 root 왼쪽의 tree(tree 는 recursive 하기에 이런 접근이 가능)의 node 갯수를 구하고, 오른쪽의 tree 의 node 갯수를 구한 뒤, root node 의 갯수인 1과 함께 더하여 반환하는 방식이다.
- time complexity: `O(N)`
- reason: 상술한 것과 같다.
### get number of terminal nodes
- description: 위의 방법과 크게 다르진 않지만, 하술한 추가 조건을 만족하는 node 의 갯수만을 counting 하는 방식이다.
  - 현재 방문한 node 가 존재한다 (`is not None`)
  - 현재 방문한 node 의 왼쪽 node 가 존재하지 않는다 (`node.left is None`)
  - 현재 방문한 node 의 오른쪽 node 가 존재하지 않는다 (`node.left is None`)
- time complexity: `O(N)`
- reason: 상술한 것과 같다.
### get number of height of tree
- description: root 기준으로 왼쪽 tree 와 오른쪽 tree 의 높이를 각각 구한다음, 두 개의 높이 중 큰 높이에 + 1 을 하여 반환하는 방식이다.
- time complexity: `O(N)`
- reason: 상술한 것과 같다.


