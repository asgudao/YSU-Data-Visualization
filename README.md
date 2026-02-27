# YSU-Data-Visualization
📊 燕山大学相关数据可视化项目，聚焦于燕山大学各类数据的采集、处理与可视化展示，旨在直观呈现学校相关维度的信息，方便分析与决策。

## 项目介绍
本项目针对燕山大学数据可视化老师提供的就业数据进行数据可视化，从而对大家的就业选择提供一定的参考。

### 核心特性
- 📈 多维度数据可视化：支持折线图、柱状图、饼图、热力图等多种图表类型
- 📝 数据解析与清洗：内置数据预处理逻辑，处理原始数据的缺失、异常值等问题
- 💻 交互友好：支持图表筛选、缩放、导出等交互功能
- 🎨 自定义样式：可灵活调整图表配色、布局，适配不同展示场景
- 📱 响应式设计：兼容PC、平板、手机等多终端访问

## 目录结构
```
YSU-Data-Visualization/
├── data/                # 数据目录（原始数据、预处理后数据）
│   ├── raw/             # 原始未处理数据
│   └── processed/       # 清洗后可直接用于可视化的数据
├── src/                 # 核心代码目录
│   ├── charts/          # 图表绘制相关代码（各类型图表实现）
│   ├── data_process/    # 数据清洗、转换、整合代码
│   ├── utils/           # 工具函数（如数据读取、格式转换）
│   └── app.js           # 项目入口文件
├── public/              # 静态资源（样式、图片、第三方库）
│   ├── css/             # 样式文件
│   ├── js/              # 第三方JS库（如ECharts、Chart.js）
│   └── images/          # 项目配图、logo等
├── docs/                # 项目文档（接口说明、数据字典等）
├── index.html           # 可视化展示主页面
├── package.json         # 项目依赖（若使用Node.js）
└── README.md            # 项目说明文档
```

## 环境准备
### 前置依赖
- 若基于前端纯静态实现：无需额外环境，现代浏览器（Chrome/Firefox/Edge等）即可
- 若包含Node.js后端/数据处理：
  - Node.js ≥ 14.x
  - npm ≥ 6.x 或 yarn ≥ 1.x

### 安装步骤
1. 克隆本仓库
```bash
git clone https://github.com/asgudao/YSU-Data-Visualization.git
cd YSU-Data-Visualization
```
2. （可选，若有Node.js依赖）安装依赖
```bash
npm install
# 或
yarn install
```

## 快速使用
### 本地运行
1. 纯静态版本：直接打开 `index.html` 文件即可查看可视化效果
2. 带Node.js服务版本：
```bash
# 启动本地服务
npm run start
# 或
node src/app.js
```
2. 访问地址：`http://localhost:3000`（端口可在配置中调整）

### 数据更新
1. 将新的原始数据放入 `data/raw/` 目录
2. 运行数据预处理脚本（若有）：
```bash
npm run process-data
```
3. 刷新页面即可查看更新后的可视化结果

## 图表类型说明
| 图表类型 | 适用场景 | 示例数据 |
|----------|----------|----------|
| 柱状图 | 对比不同类别数据（如各学院招生人数） | 各学院2024年本科招生人数 |
| 折线图 | 展示数据趋势变化（如历年就业率） | 2019-2024年全校就业率走势 |
| 饼图 | 展示数据占比（如学科分布） | 各学科硕士点数量占比 |
| 热力图 | 展示数据密度/关联度（如校园消费分布） | 校园各区域食堂消费热力 |

## 自定义配置
### 修改图表样式
在 `public/css/custom.css` 中调整图表配色、字体、尺寸等样式：
```css
/* 示例：修改柱状图颜色 */
.chart-bar {
  --color-primary: #165DFF;
  --color-secondary: #36CFC9;
}
```

### 新增图表
1. 在 `src/charts/` 目录下新建图表文件（如 `newChart.js`）
2. 编写图表绘制逻辑（基于ECharts/Chart.js等）
3. 在 `index.html` 中引入并挂载图表容器

## 贡献指南
1. Fork 本仓库
2. 创建特性分支：`git checkout -b feature/xxx`
3. 提交代码：`git commit -m 'feat: 添加xxx功能'`
4. 推送分支：`git push origin feature/xxx`
5. 提交 Pull Request


## 致谢
- 感谢 ECharts/Chart.js 等可视化库提供的技术支持
- 感谢燕山大学相关数据源提供方
- 感谢所有为本项目贡献代码的开发者

## 问题反馈
若使用过程中遇到问题，可通过以下方式反馈：
- 提交 [Issue](https://github.com/asgudao/YSU-Data-Visualization/issues)
- 联系作者：MapleLeaf000@163.com（可替换为实际联系方式）

---
⭐ 如果本项目对你有帮助，欢迎点星支持！
