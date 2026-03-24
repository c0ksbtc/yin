# 交易所自动套利资金费机器人 (Funding Rate Arbitrage Bot)

本项目是一个用于加密货币交易所之间“资金费（Funding Rate）”套利的自动化交易机器人。机器人自动��较不同交易所的资金费和标的价格差异，在满足策略与风控条件时下单，以获取无风险/相对低风险的收益机会。

## 主要功能
- 跨交易所的资金费差异监控与套利策略
- 实时价格与资金费抓取
- 可配置的交易策略与风控参数（仓位、止损、最小套利门槛等）
- 日志记录与交易记录导出
- 支持多交易所（通过 ccxt 或自定义 API 接入）

## 环境要求
- Python 3.9+
- 建议使用虚拟环境（venv 或 conda）

## 快速开始
1. 克隆仓库：
```bash
git clone https://github.com/c0ksbtc/yin.git
cd yin
```
2. 创建并激活虚拟环境：
```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate     # Windows
```
3. 安装依赖：
```bash
pip install -r requirements.txt
```
4. 复制配置示例并填写 API Key：
```bash
cp config.example.json config.json
# 编辑 config.json，将 exchange API key/secret 填写至 .env 或 config.json 中
```
5. 运行机器人（示例）：
```bash
python bot.py
```

## 配置说明
- .env：推荐放置敏感信息（交易所 API Key、API Secret）
- config.json：保存策略参数与非敏感配置（也可把所有配置放在 .env）

config.example.json 示例中包含：
- exchanges: 支持的交易所列表
- tradeAmount: 每次下单的数量（或名义仓位）
- riskLevel: 风险等级（low/medium/high）
- pollIntervalSeconds: 轮询间隔
- dryRun: 是否模拟运行

## 使用示例（重要提示）
- 首次运行请使用 dryRun=true，确认策略逻辑与下单行为正确再切换为真实交易。
- 强烈建议在小仓位与受控环境（测试账户）中验证策略。

## 风险提示
- 自动交易涉及真实资金风险，策略并非绝对无风险，市场极端波动或交易所服务异常可能造成损失。
- 请妥善保管 API Key 且仅赋予必要权限（例如禁用提现）。

## 支持的交易所
- 请在 config 中填写你要接入的交易所（示例：binance, bybit, huobi 等）

## 贡献
欢迎开源贡献。请阅读 CONTRIBUTING.md 获取贡献指南与 PR 流程。

## 许可与联系方式
- LICENSE: 项目使用 MIT 许可证（详见 LICENSE 文件）
- 如有问题请在 Issues 中提交或联系仓库所有者。

---