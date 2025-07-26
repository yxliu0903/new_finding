# 🚀 AI Architecture Discovery - 37 Move Moment

这是一个动态展示AI模型架构发现历程的交互式网页应用。通过可视化方式展示从基础架构到创新突破的演进过程，特别突出了"37 Move时刻"——架构发现的关键转折点。

## ✨ 功能特色

### 🎯 核心功能
- **动态架构展示**: 一张张架构图逐渐出现，覆盖在底图上
- **智能高亮**: 自动识别并高亮显示重要的新发现架构
- **里程碑触发**: 第37个架构触发特殊的"37 Move时刻"庆祝
- **实时统计**: 显示发现进度、新发现数量、平均分数等统计信息

### 🎨 视觉效果
- **渐变背景**: 美观的紫色渐变背景
- **动画效果**: 架构图出现时的滑入和旋转动画
- **高亮效果**: 新发现架构的金色发光边框和"NEW FINDINGS!"标签
- **响应式设计**: 适配不同屏幕尺寸

### 🎮 交互控制
- **手动控制**: 可以手动控制架构展示的进度
- **自动播放**: 支持自动连续展示所有架构
- **暂停/重置**: 随时暂停或重置展示过程
- **进度条**: 实时显示当前展示进度

## 🚀 快速开始

### 方法一：使用Python脚本（推荐）

```bash
# 进入项目目录
cd /mnt/iem-nas/home/liuyixiu/AI_Archer_local/new_finding

# 启动服务器
python3 start_server.py
```

服务器启动后会自动打开浏览器，如果没有自动打开，请手动访问：
`http://localhost:8000/index.html`

### 方法二：直接打开HTML文件

如果浏览器支持本地文件访问，可以直接双击 `index.html` 文件。

## 📊 数据结构

项目使用 `data/106.json` 文件作为数据源，每个架构条目包含：

```json
{
  "name": "架构名称",
  "name_new": "新架构名称",
  "svg_picture": "SVG架构图",
  "summary": "架构描述",
  "parameters": "参数数量",
  "score": "评分",
  "motivation": "设计动机",
  "program": "实现代码"
}
```

## 🎯 使用说明

### 基本操作
1. **开始发现之旅**: 点击开始按钮，逐张展示架构图
2. **自动播放**: 点击自动播放按钮，连续展示所有架构
3. **暂停**: 随时暂停展示过程
4. **重置**: 重置到初始状态

### 特殊功能
- **新发现识别**: 系统自动识别分数高于平均值1.5倍的架构作为新发现
- **里程碑触发**: 第37个架构会触发特殊的庆祝动画
- **实时信息**: 左侧面板显示实时统计信息
- **架构详情**: 底部显示当前架构的详细信息

## 🎨 自定义配置

### 修改高亮条件
在 `index.html` 中找到以下代码：

```javascript
// 检查是否是新发现（分数高于平均值的1.5倍）
const avgScore = this.getAverageScore();
if (arch.score > avgScore * 1.5) {
    this.markAsNewFinding(layer, arch);
}
```

可以调整倍数来改变高亮条件。

### 修改动画时间
在CSS中修改动画持续时间：

```css
.architecture-layer {
    transition: all 1.5s ease-in-out; /* 修改这里的1.5s */
}
```

### 修改里程碑触发点
在JavaScript中找到：

```javascript
if (this.currentIndex === 37 && !this.milestoneShown) {
    this.showMilestone();
}
```

修改数字37为其他值。

## 🔧 技术栈

- **前端**: HTML5, CSS3, JavaScript (ES6+)
- **样式**: CSS Grid, Flexbox, CSS Animations
- **数据**: JSON格式的架构数据
- **图形**: SVG格式的架构图
- **服务器**: Python内置HTTP服务器

## 📁 文件结构

```
new_finding/
├── index.html                     # 主页面文件
├── start_server.py                # 服务器启动脚本
├── README.md                      # 说明文档
└── data/
    └── 106.json                   # 架构数据文件
```

## 🎉 37 Move时刻

"37 Move时刻"象征着AI架构发现的关键转折点，就像围棋中的关键一步一样，第37个架构代表着一个重要的突破或发现。这个时刻会触发特殊的庆祝动画，标志着架构发现历程中的一个重要里程碑。

## 🤝 贡献

欢迎提交Issue和Pull Request来改进这个项目！

## 📄 许可证

本项目采用MIT许可证。 