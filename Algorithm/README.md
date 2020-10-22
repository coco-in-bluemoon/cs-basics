## 정렬(Sorting)

### O(N*N) 정렬
1. **[버블 정렬(Bubble Sort)](./code/sorting_bubble.py)**
    - 가장 비효율적: 비교 연산과 swap 연산이 다른 O(N*N) 정렬보다 많다
2. **[선택 정렬(Selection Sort)](./code/sorting_selection.py)**
3. **[삽입 정렬(Insertion Sort)](./code/sorting_insertion.py)**
    - (그나마) 가장 효율적: 정렬된 상태라면 가장 효율적으로 정렬 여부 판단 가능

### O(N*logN) 정렬
1. **[퀵 정렬(Quick Sort)](./code/sorting_quick.py)**
   - 피벗을 잘못 설정하는 최악의 경우 O(N*N)까지 시간 복잡도가 증가
2. **[병합 정렬(Merge Sort)](./code/sorting_merge.py)**
   - 항상 절반으로 나누기 때문에 O(N*logN) 보장
   - 메모리를 많이 사용으로 인해 비효율적
3. **[힙 정렬(Heap Sort)](./code/sorting_heap.py)**
   - 힙 자료 구조를 활용
   - 효율적인 메모리 사용 하지만 퀵 정렬보다는 느리다
   - 과정: 최대 힙 구축 → 첫 번째 원소를 마지막 원소로 변경 → 나머지 배열에 대해서 힙 구축

### O(N) 정렬
1. **[개수 정렬(Count Sort)](./code/sorting_count.py)**
   - 배열을 한 번 순회하여서 개수를 세는 정렬 방법
   - 일반적이지 않다

**퀵 정렬을 사용하는 것이 빠르다.**  
**하지만 최악의 경우 O(N\*N)이기 때문에 O(N logN)을 보장하는 병합 정렬을 사용할 것이다.**  
**물론 삽입 정렬로 정렬 여부 판단하고 퀵 정렬로 최종 정렬하는 것도 좋은 방법이라고 생각한다.**  
