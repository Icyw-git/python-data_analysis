# 数学建模与数据分析学习项目

本项目是一个综合性的数学建模和数据分析学习仓库，涵盖了多种评价决策方法、数据分析技术和可视化技能的学习与实践。

## 项目概述

本项目主要包含以下内容：

- **评价决策方法**：层次分析法(AHP)、熵权法、TOPSIS法
- **数据分析工具**：NumPy、Pandas、Matplotlib、Seaborn
- **实际案例分析**：电影数据分析、RFM客户分析、电商销售分析

## 项目结构

```
math1/
├── data/                          # 数据集目录
│   ├── 1960-2019全球GDP数据.csv   # 全球GDP历史数据
│   ├── iris.csv                   # 鸢尾花数据集
│   ├── movie.csv                  # 电影数据集
│   ├── rfm.xlsx                   # RFM分析数据
│   ├── sales.xlsx                 # 销售数据
│   ├── stock_day.csv              # 股票日线数据
│   ├── uniqlo.csv                 # 优衣库销售数据
│   ├── my_file.csv                # 示例数据文件
│   ├── shanghai.png               # 上海地图图片
│   ├── context                    # 上下文文件
│   └── Topsis.py                  # TOPSIS算法实现
│
├── 1-层次分析法【微信公众号丨B站：数模加油站】.ipynb  # 层次分析法教程
├── RFM案例.ipynb                  # RFM客户价值分析案例
├── 电影分析练习.ipynb              # 电影数据分析练习
├── 电商销售分析.ipynb              # 电商销售数据分析
├── matplotlib seaborn绘图.ipynb   # 数据可视化教程
├── numpy示例.ipynb                # NumPy学习笔记
├── pandas.ipynb                   # Pandas学习笔记
├── pandas的基本操作.ipynb          # Pandas基础操作
│
├── demo1.py                       # 层次分析法示例代码
├── 熵权法.py                       # 熵权法实现
├── np库.py                        # NumPy库练习
├── pd库.py                        # Pandas库练习
│
├── readme.md                      # 项目说明文档
└── .gitignore                     # Git忽略文件配置
```

## 核心内容详解

### 1. 评价决策方法

#### 层次分析法 (AHP)

- **文件**：`demo1.py`, `1-层次分析法.ipynb`
- **功能**：通过构建层次结构模型，进行多准则决策分析
- **核心步骤**：
    - 构建判断矩阵
    - 计算特征值和特征向量
    - 一致性检验(CR < 0.1)
    - 计算权重和综合得分

#### 熵权法

- **文件**：`熵权法.py`
- **功能**：基于信息熵理论客观确定指标权重
- **核心步骤**：
    - 数据标准化处理
    - 计算信息熵
    - 计算信息效用值
    - 确定指标权重

#### TOPSIS法

- **文件**：`data/Topsis.py`
- **功能**：逼近理想解排序法，用于多属性决策
- **支持指标类型**：
    - 极大型指标
    - 极小型指标
    - 中间型指标
    - 区间型指标

### 2. 数据分析工具

#### NumPy

- **文件**：`numpy示例.ipynb`, `np库.py`
- **内容**：
    - 数组创建与操作
    - 数学运算与线性代数
    - 随机数生成
    - 广播机制

#### Pandas

- **文件**：`pandas.ipynb`, `pandas的基本操作.ipynb`, `pd库.py`
- **内容**：
    - DataFrame和Series操作
    - 数据读取与写入
    - 数据清洗与预处理
    - 分组聚合与透视表
    - 数据合并与连接

#### 数据可视化

- **文件**：`matplotlib seaborn绘图.ipynb`
- **内容**：
    - Matplotlib基础绘图
    - Seaborn高级可视化
    - 统计图表绘制
    - 图表美化与定制

### 3. 实际案例分析

#### 电影数据分析

- **文件**：`电影分析练习.ipynb`
- **数据集**：`data/movie.csv`
- **分析内容**：
    - 评分分布统计
    - 电影类型分析
    - 年度趋势分析
    - 类型流行趋势

#### RFM客户分析

- **文件**：`RFM案例.ipynb`
- **数据集**：`data/rfm.xlsx`
- **分析内容**：
    - 客户价值分层
    - RFM模型构建
    - 客户细分策略

#### 电商销售分析

- **文件**：`电商销售分析.ipynb`
- **数据集**：`data/sales.xlsx`, `data/uniqlo.csv`
- **分析内容**：
    - 销售趋势分析
    - 商品类别分析
    - 时间序列分析

## 快速开始

### 环境要求

- Python 3.7+
- Jupyter Notebook
- 必要的Python库：
  ```bash
  pip install numpy pandas matplotlib seaborn openpyxl
  ```

### 使用说明

1. **学习评价方法**：
    - 打开 `1-层次分析法.ipynb` 学习AHP方法
    - 运行 `熵权法.py` 了解熵权法实现
    - 查看 `data/Topsis.py` 学习TOPSIS算法

2. **掌握数据分析工具**：
    - 从 `numpy示例.ipynb` 开始学习NumPy
    - 通过 `pandas的基本操作.ipynb` 掌握Pandas
    - 使用 `matplotlib seaborn绘图.ipynb` 学习可视化

3. **实践案例分析**：
    - 运行 `电影分析练习.ipynb` 进行电影数据分析
    - 参考 `RFM案例.ipynb` 进行客户价值分析
    - 学习 `电商销售分析.ipynb` 的销售分析方法

## 数据集说明

| 文件名                  | 描述      | 用途        |
|----------------------|---------|-----------|
| movie.csv            | 电影信息数据  | 电影类型、评分分析 |
| iris.csv             | 鸢尾花数据集  | 分类算法练习    |
| rfm.xlsx             | 客户交易数据  | RFM客户价值分析 |
| sales.xlsx           | 销售记录数据  | 销售趋势分析    |
| uniqlo.csv           | 优衣库销售数据 | 零售数据分析    |
| stock_day.csv        | 股票日线数据  | 金融数据分析    |
| 1960-2019全球GDP数据.csv | 全球经济数据  | 时间序列分析    |

## 学习路径建议

### 初学者路径

1. 先学习 `numpy示例.ipynb` 掌握数组操作
2. 学习 `pandas的基本操作.ipynb` 掌握数据处理
3. 运行 `demo1.py` 理解层次分析法
4. 完成 `电影分析练习.ipynb` 进行综合实践

### 进阶学习路径

1. 深入研究 `熵权法.py` 和 `data/Topsis.py`
2. 完成 `RFM案例.ipynb` 和 `电商销售分析.ipynb`
3. 学习 `matplotlib seaborn绘图.ipynb` 提升可视化能力
4. 尝试将多种评价方法结合使用

## 贡献与反馈

本项目主要用于个人学习和练习，欢迎提出改进建议。

## 许可证

本项目仅供学习交流使用。

---

**注意**：部分教程内容参考了"数模加油站"的公开资料，感谢原作者的分享。