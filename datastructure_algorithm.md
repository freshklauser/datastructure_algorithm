[TOC]

## 1. 数据结构

### 1.1 基础类型

#### 1.1.1 基本数据类型

##### 1.1.1.1 输入输出

- `format`数字格式化

  ```
  '{}:{:0>2d}'.format(5, 5)
  Out[60]: '5:05'
  
  # 进制format
  '{:b}:{:0>2d}'.format(15, 5)
  Out[71]: '1111:05'
  '{:o}:{:0>2d}'.format(15, 5)
  Out[72]: '17:05'
  '{:d}:{:0>2d}'.format(15, 5)
  Out[73]: '15:05'
  '{:x}:{:0>2d}'.format(15, 5)
  Out[74]: 'f:05'
  '{:#x}:{:0>2d}'.format(15, 5)
  Out[75]: '0xf:05'
  ```

  - `b、d、o、x` 分别是二进制、十进制、八进制、十六进制
  - `^, <, > `分别是居中、左对齐、右对齐，后面带宽度， `:` 号后面带填充的字符，只能是一个字符，不指定则默认是用空格填充。
  - `+ `表示在正数前显示` +`，负数前显示`-`；  `空格`表示在正数前加空格

  <div align=center><img src='E:\_Jun\_Python\_Repos_ds_algo\datastructure_algorithm\image\format.PNG' width=90%></div>

#### 1.1.2 进制转换

##### 1.1.2.1 位运算实现进制转换

- 正数转化位十六进制（见负数转化过程介绍）
- 负数转化位十六进制 --- 负数转化位正数再按正数的进制转化处理
  - 32位有符号最大值： MAX = `0xffffffff`    (16位：`0xffff` )   --- （`0xf=0b1111`）
  - `python`中<font color=red>负数`num`转为正数</font>： <font color=red>`num &= 0xffffffff`</font>
  - `num`取二进制低4位借助掩码<font color=red>`0b1111`</font>：<font color=red> `target = num & 0b1111`</font> 
  - 十六进制符号： `hex_mapper='0123456789abcdef'`
  - 低4位转16进制： `hexer = hex_mapper[num & 0b1111]`
  - 右移低4位，获取下一个进制转换： `num = num >> 4`

#### 1.1.3 原码、反码、补码

##### 1.1.3.3 补码

- python中没有符号位一说，即使有符号位，在python看来都是正数（`a=0xffffffff`在python中-1的32补码， `4294967295, 即2**32 - 1`）

  ```
  print(0xffffffff & -5, -5 & -1)  # 4294967291 -5
  ```

- python 中负数前面有无限个 1 表示负数，比如 `5` 的补码是 `(0)_infinite 101`，而 `-5` 的补码是 `(1)_infinite 011`，也就是前面有无限个 `1`，因此获取负数的补码直接用 `hex` 或者 `bin` 是行不通的。

  ````
  In [193]: bin(-5),hex(-5),0xffffffff, 0xffffffff&-5, -5&-1
  Out[193]: ('-0b101', '-0x5', 4294967295, 4294967291, -5)
  ````

- **针对负数`num`，调用`hex`或`bin`之前需要先把负数转化位正数**，即<font color=red> `num = num & 0xffffffff` 将负数转化为正数</font>。

- 使用 `&` 操作符，把负数前置无限个 `1` 和 正数 `0xFFFFFFFF` 前置无限个 `0` 与运算，那么负数前置的 `1` 全部被干掉成为 `0`,即成为正数，是 python 中获取 【x 位整型】补码形式的一种操作。

  ```
  In [201]: -5 & 0xffffffff,-5+2**32, -12 & 0xffffffff, -12+2**32, 2**32
  Out[201]: (4294967291, 4294967291, 4294967284, 4294967284, 4294967296)
  ```

  如上述代码，可以理解为： -5 = -5 + MAX,   +5=+5

#### 1.1.4 位运算

- `int`类型数据转化为<font color=red>二进制层面的运算</font>

- 运算符优先： `<<  >>` 大于 `+=  -= `

  <div align=center><img src='E:\_Jun\_Python\_Repos_ds_algo\datastructure_algorithm\image\运算符优先级.PNG'></div>

##### 1.1.4.1 位运算汇总表

- 位运算只支持 `int`类型数据
- 按位 与     `&`:  两个为1，则结果为1；否则结果为0 （`0&0=0&1=1&0=0，1&1=1`）
- 按位 或     `|`：至少一个为1，则结果为1；否则结果为0 (`0|1=1|0=1|1=1，0|0=0`)
- 按位 异或  `^`: 相异为1，相同为0  (`0^0=1^1=0，0^1=1^0=1`)

<div align=center><img src='E:\_Jun\_Python\_Repos_ds_algo\datastructure_algorithm\image\位运算.PNG'></div>

- `<<` 左移： 原来的所有位左移，高位丢弃，低位补0，相当于 <font color=red>`乘以2`</font>

- `>>`  右移：各二进位全部右移若干位，对无符号数，高位补0，有符号数，各编译器处理方法不一样，有的补符号位（算术右移），有的补0（逻辑右移） 相当于 <font color=red>`地板除2`</font>

##### 1.1.4.2 位运算常用场景

- 与 ：

  - <font color=red>`x&mask` </font>实现掩码，只保留想要的位置的数字

  - 判断奇偶： <font color=red>`x&1`</font>  <font color=skyblue>（二进制数以1结尾是奇数，以0结尾是偶数）</font>

    `odd & 1 == 1 --> 奇数`

    `even & 1 == 0 --> 偶数`

  - <font color=red>`x&(x-1)`</font>可以删除最低位的一个1 （???? 直接 `x-1`不就时删除了最低位的`1` ????）

    ```
    # 判断一个数是否时2的幂  （特征：二进制只有1个1，减去1则后续的0全变为1）
    # 2**4 - 1 = 2**3 + 2**2 + 2**1 + 1 --> 二进制： 00010000 --> 00001111
    # --> 2**n & (2**n - 1) == 0 即 if x&(x-1)==0,则x为2的幂
    ```

- 异或： <font color=red>任何数和`0`异结果为其自身， 任何数和其自身异或结果为`0`</font>
  - 位级反转

  - 数据去重

    ```
    0^23^12^12^42^23
    Out[38]: 42
    0^23^12^12^42^42^23
    Out[39]: 0
    ```

    ```
    # 示例：输入一个整数，输出该数二进制表示中 1 的个数
    # 思路：
    	思路1：n//=2遍历n, n%2==1计数，
    	思路2：与运算& 和 右移>>
    def hamming_weight(number):
    	count = 0
    	while number:
    		count += number&1
    		number >> 1
    	return count
    ```

    

- 加法计算原理

  ```
  # (a + b) / 2  ----> (进位移高一位 + 无进位和)/2 => ((a & b)<<1 + (a ^ b))>>1
  ```




## 2. 查找算法
### 2.1 算法概览
#### 2.1.1 常用查找算法的复杂度
<div align=center><img src="E:\_Jun\_Python\_Repos_ds_algo\datastructure_algorithm\abstract\sorts\images\查找算法时间复杂度.PNG", width=100%></div>

### 2.2 顺序查找

### 2.3 二分查找  ---- 暂不要求

### 2.4 散列(Hashing)
#### 2.4.1 基本概念
- 实现从数据项到存储槽名称的转换的成为散列函数（hash function）
- 冲突`collisiont` 与 解决冲突方案
- 完美散列函数
- 好的散列函数特性：冲突最小，计算难度低（额外开销小），充分分散数据项（节约空间）
- 用途：

    数据一致性校验：由任意长度的数据生成长度固定的“指纹”，还要求具备唯一性
    
    数据一致性校验的“指纹”函数需具备特征：
    - 压缩性：任意长度的数据，得到的指纹长度是固定的
    - 易计算性
    - 抗修改性：对原数据的微小改动，都会引起“指纹”的大改变
    - 抗冲突性
#### 2.4.2 散列函数
##### 2.4.2.1 `MD5`/`SHA `



#### 2.4.3 常用散列方法
##### 2.4.3.1 求余数 
- 将数据项除以散列表的大小，得到的余数作为槽号（见2.4.2示例1）

    由于散列函数返回的槽号必须在散列表大小范围内，所以一般会对散列表大小求余

#### 2.4.3 示例
- 示例1：

    散列函数接收数据先作为参数，返回整数值0-10， 表示数据项存储的槽号（名称）
    





## 3. 排序算法
### 3.1 算法概览



#### 3.1.1 常用排序算法时间复杂度
<div align=center><img src="E:\_Jun\_Python\_Repos_ds_algo\datastructure_algorithm\abstract\sorts\images\排序算法时间复杂度.PNG", width=100%></div>

### 3.2 冒泡排序 （两两相邻比较，每次比较均可能交换数据）

- 概念：对无序表进行**多趟 比较交换**，每趟包括了多次两两相邻比较，并将逆序的数据项互换位置，最终能将本躺的最大值移到最后

- 思路：遍历，比较两两相邻数据，将大的往后移，遍历一遍之后最大值就在最后(此时需要遍历的数据减少为（n-1）

- 建议： <font color=orange>反向遍历，正向比较交换</font> （**每比较一次就交换一次数据**）

- 可能改进：变量记录是否交换，若一趟遍历完始终没有发生过数据交换，则表明数据已经有序，可提前结束遍历

- 代码

  ```
  def bubble(seq):
      """
      反向遍历，两两比较，比较的同时伴随则数据交换
      :param seq:
      :return:
      """
      length = len(seq)
      for cur_len in range(length - 1, 0, -1):           # start = length - 1
          exchange = False
          for i in range(cur_len):
              if seq[i + 1] < seq[i]:
                  # exchange data each time when compared if later is lt former
                  seq[i], seq[i + 1] = seq[i + 1], seq[i]
                  exchange = True
          if not exchange:
              break
      return seq
  ```

### 3.3 选择排序 （两两相邻比较，记录较大值index, 与最后一项数据比较后数据交换）

- 基于冒泡排序的改进：减少数据交换次数

- 改进点： 记录两两比较值的较大值的index, 遍历到最后一个数时数据交换。**每趟比较只发生了一次数据交换**。

- 建议： <font color=orange>反向遍历，正向比较维护`max`的`index`</font> （**最后一次才交换数据**）

- 代码：

  ```
  def select(seq):
      """
      两两对比，每次记录最大值位置，每趟遍历的最后一次比较时触发数据交换
      :param seq:
      :return:
      """
      length = len(seq)
      for cur_len in range(length - 1, 0, -1):        # start = length - 1
          position_swap = False
          marker = 0
          for i in range(1, cur_len + 1):             # start = 1, end = cur_len + 1 
              # mark the index of larger value
              if seq[i] > seq[marker]:
                  marker = i
                  position_swap = True
              # consider data exchange when one loop end
              if marker != cur_len:
                  seq[i], seq[marker] = seq[marker], seq[i]
          if not position_swap:
              break
      return seq
  
  ```

### 3.4 插入排序 （【有序子列表  |  无序子列表】）

- 基本思想：类比扑克，维持一个已经排序好的子列表，其位置始终在列表前部，然后逐步扩大这个子列表直至全表

- 【有序子列表 | 无序子列表】

- 步骤：

  - 第一趟，子列表包含第一个数据项，将第二个作为新项插入到子列表合适位置，此时子列表为2个数据项的有序子列表；
  - 第二趟，将第三个数据跟前两个比对，并移动到刚好比自身大的数据项的前一个位置，此时子列表为3个数据项的有序子列表；
  - 经过n-1趟比对和插入，子列表扩展到全表，完成排序

- 建议： <font color=orange>正向遍历无序列表元素，反向遍历有序列表插入</font>

- 代码

  ```
  def insert(seq):
      """
      类比扑克，【有序列表 | 无序列表】
      正向遍历无序列表元素a(index:[1,...,length-1])，反向遍历有序列表进行对比，
      比a大的元素后移一位，直至碰到比a小的b，将a元素插入到b之后,跳出反向遍历
      :param seq:
      :return:
      """
      length = len(seq)
      for i in range(1, length):     # end = length - 1
          position = i
          target = seq[position]
          while position > 0 and seq[position - 1] > target:
              seq[position] = seq[position - 1]
              position -= 1
          seq[position] = target
      return seq
  ```

### 3.5 谢尔排序 `Shell sort` （间隔划分的多子表插入排序）
- 谢尔排序以插入排序为基础，对无序表进行<font color=red>**间隔**</font>划分子列表，每个子列表执行插入排序。按下标相隔距离为gap分的组，也就是说把下标相差gap的分到一组,比如，间隔`gap`=4, 则把`0,4,8,12`分到一组，`1,5,9,13`一组，`2,6,10,14`一组，`3，7，11，15`一组，间隔为4，一共分成4住

- 子列表的间隔一般从 `n/2` 开始，**逐步成倍缩小间隔**： `n/4, n/8 ......` 直到1.

- 不稳定算法

- 步骤：在插入排序的外层加一个增量`gap`的循环,`gap /= 2`

- 代码：

  ```
  def sheller(seq):
      """
      间隔gap的数据为一组（逻辑分组，不是物理分组），间隔划分后的子列表个数=gap
      gap初始 n/2, 成倍递减 （n/4, n/8,.., 1）,针对每组插入排序
      :param seq:
      :return:
      """
      def gap_insert(seq, start, gap):
          for i in range(start + gap, len(seq), gap):
              position = i
              target = seq[i]
              while position >= gap and seq[position - gap] > target:
                  seq[position] = seq[position - gap]
                  position -= gap
  
              seq[position] = target
  
      length = len(seq)
      gap = length // 2
      while gap >= 1:
          for start_point in range(gap):
              gap_insert(seq, start_point, gap)
          gap //= 2
      return seq
  ```

### 3.6 归并排序   --- 暂不要求

- 思路：分裂，归并

### 3.7 快速排序 （中值分裂成左右两部分后递归）

- 快速排序是一种**不稳定**的排序算法，即**多个相同的值的相对位置也许会在算法结束时产生变动**。

- 思路：分解，分裂

  依据一个 <font color=orange>中值</font> 数据把数据表分<font color=orange>两半</font>：(1) 小于中值的一半； (2) 大于中值的一半。然后每部分分别快速排序（递归）

- 分裂数据表的目标： 找到 中值即分裂点 的位置 （初始设置中值为第一个元素）

- <font color=orange>在找分裂点的过程中即实现了排序</font>

- 分裂点查找方式：**左右指针法**

  - 左指针向右移动，碰到比 中值 大的就停下，记录当前指针位置
  - 右指针向左移动，碰到比 中值 小的就停下，记录当前指针位置
  - 交换左右指针指向的数据 （小的交换到了中值左边，大的交换到了中值右边）
  - 继续移动左右指针，直到左指针移动到右指针的右边，此时右指针位置就时 中值 应该所处的位置，将中值和这个位置交换 （因为右指针指向的时比中值小的，因此只能将右指针位置的数据与中值初始值0索引的数据交换）
  - 分裂完成，左半部比中值小，右半部比中值大 （不一定有序）
  - 针对左右两部分，分别调用自身

- 代码：

  ```
  def quick(items):
      """
      找分裂点（过程中即已经实现排序），分别对分裂点左右两半部分调用自身
      :param items:
      :return:
      """
      left = 0
      right = len(items) - 1
      quick_helper(items, left, right)
      return items
  
  
  def quick_helper(items, left, right):
      if left < right:
          split_point = partition(items, left, right)
          # print(split_point, items)
          quick_helper(items, left, split_point - 1)
          quick_helper(items, split_point + 1, right)
  
  
  def partition(items, left, right):
      pivot_value = items[left]
      left_cursor = left + 1
      right_cursor = right
  
      done = False
      while not done:
          # 左指针向右移动，遇到大于初始基准值时停止，此时左指针指向的是大于基准值的位置
          while left_cursor <= right_cursor and items[left_cursor] <= pivot_value:
              left_cursor += 1
          # 右指针向左移动，遇到小于初始基准值时停止，此时右指针指向的是小于基准值的位置
          while right_cursor >= left_cursor and items[right_cursor] >= pivot_value:
              right_cursor -= 1
  
          # 当右指针移到了左指针的左边，说明已经找了分裂点，即右指针指向的点, 交换右指针和基准值的位置
          if right_cursor < left_cursor:
              # 对初始基准值排序：初始基准值与右指针指向的点交换位置（即初始基准值找到了正确的位置）
              items[left], items[right_cursor] = items[right_cursor], items[left]
              done = True
          # 左右指针停止后，两个指针指向的数据交换位置，即排序
          else:
              items[left_cursor], items[right_cursor] = items[right_cursor], items[left_cursor]
  
      return right_cursor
  
  if __name__ == '__main__':
      items = [87, 6, 65, 12, 33, 2, 98, 3, 43, 23, 51]
      print(quick(items))
  ```

- 图解：

  <div align=center><img src='E:\_Jun\_Python\_Repos_ds_algo\datastructure_algorithm\abstract\sorts\images\quicksort1.PNG' width=70%></div>

### 3.8 堆排序

#### 3.8.1 基本概念

- 堆排序是利用**堆(完全二叉树)**这种数据结构而设计的一种排序算法，堆排序是一种**选择排序**

- 大顶堆： **每个结点的值都大于或等于其左右孩子结点的值**

  ​	        **arr[i] >= arr[2i+1] && arr[i] >= arr[2i+2]**    

- 小顶堆：**每个结点的值都小于或等于其左右孩子结点的值**

  ​		**arr[i] <= arr[2i+1] && arr[i] <= arr[2i+2]**

-  堆排序（完全二叉树）最后一个非叶子节点的序号是 `n/2-1` (向下取整)  [原因](https://www.cnblogs.com/malw/p/10542557.html) 

- 性质：

  （1）查找数组(0开始索引)中某个数的父结点和左右孩子结点，比如已知索引为 **i** 的数，那么

  ​	1.<font color=orange>父结点索引：`(i-1)//2`</font>

  ​	2.左孩子索引：`2*i+1`

  ​	3.右孩子索引：`2*i+2`

  （2）非叶子节点个数

  ​	最后一个非叶子节点索引计算：求 最后一个叶子节点的父节点即可 

  ```
  # tree_length = n
  last_node_index = n - 1
  parent_node_index =  (last_node_index - 1) // 2
  
  ```

  

#### 3.8.2 基本实现

- 1.首先将待排序的数组构造成一个大根堆，此时，整个数组的最大值就是堆结构的顶端

- 2.将顶端的数与末尾的数交换，此时，末尾的数为最大值，剩余待排序数组个数为`n-1`

- 3.将 ·剩余的 `n-1`个数再构造成大根堆，再将顶端数与`n-1`位置的数交换，如此反复执行，便能得到有序数组

  原则： <font color=orange>升序用大根堆，降序就用小根堆</font>

- 代码：

  ```
  """
  堆排序过程：
  1、构将大根堆：将待排序数组构造成一个大根堆（元素上升） -- build_heap 非叶子节点逆序递归调用heapify
     确定最后一个非叶子节点（即last_node的parent_node）的index, 从这个点开始逆序遍历数组，对每个索引做heapify即可构造出大顶堆。
     其中，heapify函数中，对于每次最大值交换影响到的节点，需要递归调用heapifty实现受影响节点的堆化
  2、固定一个最大值，由于大根堆的节点已经部分有序（父节点大于左右节点），秩序堆0节点做heapify即可
     遍历剩下节点的tree, 将根节点元素最大元素和最后一个元素交换位置，固定该最大值，将剩余的节点再构建大根堆
  """
  
  
  def heaq_sort(tree):
      number = len(tree)
      build_heap(tree, number)
      for i in range(number - 1, 0, -1):
          # 交换堆顶最大值和最后一个节点，固定最大值
          tree[i], tree[0] = tree[0], tree[i]
          # 对当前堆(tree节点一直在减少，数量由i决定)的顶根节点做heapify即可
          heapify(tree, i, 0)
      return tree
  
  
  def build_heap(tree, node_num):
      """
      对节点个数为 node_num 的数组构建大顶堆 (对节点调用heapify)
      思路：
          从最后一个非叶子节点开始，逆序遍历至根节点，堆每一个遍历的节点heapify
      :param tree:     当前待排序的数组
      :param node_num: 堆从根节点0处到索引 node_num - 1 处的 node_num 个节点
      :return:
      """
      last_node_index = node_num - 1
      parent_index = (last_node_index - 1) // 2
      for i in range(parent_index, -1, -1):
          heapify(tree, node_num, i)
  
  
  def heapify(tree, node_num, index):
      """
      对数组中索引为index的节点做heapify (3个节点的根节点最大化)
      在heapify过程中，由于最大值的数据交换影响到的节点需递归调用heapify
      原址交换，不需要额外辅助空间
      示例： [4, 7, 3] --> [7, 4, 3]
      :param tree:     带排序的数组
      :param node_num: 当前堆的节点数
      :param index:    heapify操作的节点
      :return:
      """
      if index >= node_num:
          return None
      left_node = 2 * index + 1
      right_node = 2 * index + 2
      max_index = index
      if left_node < node_num and tree[left_node] > tree[max_index]:
          max_index = left_node
      if right_node < node_num and tree[right_node] > tree[max_index]:
          max_index = right_node
      if max_index != index:
          # 最大值的点不是指定的index节点，需要交换数据将最大值交换到index
          tree[max_index], tree[index] = tree[index], tree[max_index]
          # 对交换后的max_index索引位的节点递归调用堆化
          heapify(items, node_num, max_index)
  
  
  if __name__ == '__main__':
      items = [12, 43, 6, 23, 98, 33, 65, 2, 3, 87, 51]
      res = heaq_sort(items)
      print(res)
  ```

## 4. 字符串

### 4.1 回文字符串  -- 双指针法

- 回文字符串基本解法： <font color=font>双指针法</font>

- 总体思路：设置<font color=red>头尾指针</font>，如果双指针的字符相同，指针往中间挪动，继续检查

  



## 附录

### A1 - `collections`

REFER: https://www.cnblogs.com/dianel/p/10787693.html

#### `from collections import Counter` `计数器 (item, counter)`

- 作用：字典的子类（返回结果为字典`{element: counts}`），提供了可哈希对象的计数功能，对象包括 列表，元组，集合、字符串、字典等

```
In [48]: from collections import Counter
In [49]: alist = list('andhyeasdbdd')
In [50]: cnt = Counter(alist)
In [51]: cnt
Out[51]: Counter({'a': 2, 'n': 1, 'd': 4, 'h': 1, 'y': 1, 'e': 1, 's': 1, 'b': 1})
```

- 常用方法：
  - `elements()`：返回一个<font color=red>迭代器</font>，每个元素重复计算的个数，如果一个元素的**计数小于1, 就会被忽略**。
  - `most_common([n])`：返回一个列表，提供`n`个<font color=red>访问频率最高的元素和计数</font> `(element, count)`
  - `subtract([iterable-or-mapping])`：从迭代对象中减去元素，输入输出可以是0或者负数
  - `update([iterable-or-mapping])`：从迭代对象计数元素或者从另一个 映射对象 (或计数器) 添加。

```
# 查看元素
In [80]: cnt.items()
Out[80]: dict_items([('a', 2), ('n', 1), ('d', 4), ('h', 1), ('y', 1), ('e', 1), ('s', 1), ('b', 1)])
In [81]: cnt.keys()
Out[81]: dict_keys(['a', 'n', 'd', 'h', 'y', 'e', 's', 'b'])
In [82]: cnt.values()
Out[82]: dict_values([2, 1, 4, 1, 1, 1, 1, 1])
In [89]: cnt['a']
Out[89]: 2
In [94]: cnt.get('i', 0)	# key不存在则默认返回0
Out[94]: 0

# 获取元素或出现频次
In [55]: cnt.most_common()
Out[55]: 
[('d', 4),
 ('a', 2),
 ('n', 1),
 ('h', 1),
 ('y', 1),
 ('e', 1),
 ('s', 1),
 ('b', 1)]
In [56]: cnt.most_common(2)
Out[56]: [('d', 4), ('a', 2)]

# 追加对象 counter1.update(counter2)（不返回值，原址修改） 或者 c + d（生成新counter，需返回值）
In [96]: ext = Counter(list('xzz'))
In [97]: cnt.update(ext)
In [98]: cnt.items()
Out[98]: dict_items([('a', 2), ('n', 1), ('d', 4), ('h', 1), ('y', 1), ('e', 1), ('s', 1), ('b', 1), ('x', 1), ('z', 2)])

# 减少对象，c.subtract(d)（key保留，值为0，原址修改） ，或者 c - d (key也删除掉，需返回值)
In [112]: cnt - ext
Out[112]: Counter({'a': 2, 'n': 1, 'd': 4, 'h': 1, 'y': 1, 'e': 1, 's': 1, 'b': 1})

# 清除
In [155]: ext.clear()
In [156]: ext
Out[156]: Counter()
```

### A2 - `itertools`

  #### `from itertools import product` ``笛卡尔积` 

```
In [33]: for i in itertools.product(['a','b'], list('ef')):
    ...:     print(i)

('a', 'e')
('a', 'f')
('b', 'e')
('b', 'f')
```

#### `from itertools import permutations`  `排列 A(m,n)` `不放回抽样排列`

```
In [35]: for i in itertools.permutations('ABD', 3):
    ...:     print(i)
    ...: 
('A', 'B', 'D')
('A', 'D', 'B')
('B', 'A', 'D')
('B', 'D', 'A')
('D', 'A', 'B')
('D', 'B', 'A')
```

#### `from itertools import combinations` `组合 C(m,n) 无返回抽样组合`

```
In [37]: for i in itertools.combinations('ABD', 2):
    ...:     print(i)
    ...: 
('A', 'B')
('A', 'D')
('B', 'D')
```

#### `from itertools import combinations_with_replacement ` `组合 有放回抽样组合`

```
In [38]: for i in itertools.combinations_with_replacement('ABD', 2):
    ...:     print(i)
    ...: 
('A', 'A')
('A', 'B')
('A', 'D')
('B', 'B')
('B', 'D')
('D', 'D')
```

### A3 字符串内置方法

```
str.count(str, beg=0, end=len(string))  		# 返回 str 在 string 里面出现的次数
str.startswith(obj, beg=0, end=len(string))		
str.endswith(obj, beg=0, end=len(string))		

str.isalnum()		#  string 至少有一个字符并且所有字符都是字母或数字
str.isalpha()
str.isdigit()		# 如果 string 只包含数字则返回 True 否则返回 False.
str.isnumeric()		# 如果 string 中只包含数字字符，则返回 True，否则返回 False
```



