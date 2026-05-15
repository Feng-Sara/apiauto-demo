# Demo API 服务

简单用户 API：登录、用户 CRUD，数据存于内存。用于本仓库接口自动化测试演示。

## 依赖

需已安装项目依赖（含 Flask）：

```bash
# 在项目根目录
pip install -r requirements.txt
# 或
python3 -m pip install -r requirements.txt
```

## 启动

```bash
# 方式一：在 demo_project 目录下
cd demo_project
python app.py
# 或
python3 app.py

# 方式二：在项目根目录
python demo_project/app.py
```

- 默认端口 **11011**，可通过环境变量 `DEMO_PORT` 修改，例如：`DEMO_PORT=8080 python app.py`
- 服务地址：http://localhost:11011

## 演示账号

| 用户名 | 密码   |
|--------|--------|
| admin  | admin123 |
| test   | test123  |

## 认证说明

- **登录**：`POST /auth/login` 请求体 `{"username","password"}`，响应中返回 `data.token`
- **需认证接口**：请求头携带 `Authorization: Bearer <token>`
- 统一响应格式：`{"code": 200, "msg": "success", "data": ...}`

## 接口列表

| 方法 | 路径 | 说明 | 认证 |
|------|------|------|------|
| POST | /auth/login | 登录，返回 token | 否 |
| GET  | /api/v1/user | 获取当前用户信息 | 是 |
| GET  | /api/v1/users | 用户列表 | 是 |
| POST | /api/v1/users | 创建用户 | 是 |
| GET  | /api/v1/users/{id} | 获取指定用户 | 是 |
| PUT  | /api/v1/users/{id} | 更新用户 | 是 |
| DELETE | /api/v1/users/{id} | 删除用户 | 是 |

### 请求/响应示例

**登录**

```bash
curl -X POST http://localhost:11011/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"admin123"}'
```

响应：`{"code":200,"msg":"success","data":{"token":"...","userId":"..."}}`

**获取当前用户（需 token）**

```bash
curl -X GET http://localhost:11011/api/v1/user \
  -H "Authorization: Bearer <你的token>"
```

**创建用户**

```bash
curl -X POST http://localhost:11011/api/v1/users \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"username":"newuser","password":"pass123","email":"new@demo.com"}'
```

## 与自动化测试配合

本 Demo 服务可直接作为自动化测试目标。在项目根目录：

1. 启动本服务：`python demo_project/app.py`
2. 执行 Excel 用例时指定：`--base-url http://localhost:11011`，并配置 `TEST_USER=admin`、`TEST_PASS=admin123`（或使用 `config/env.example` 中的变量）。

详见项目根目录 [README.md](../README.md)。
