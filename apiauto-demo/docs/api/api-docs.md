# 用户 API 接口文档（自动生成）

生成时间：2026-05-15  
项目：apiauto-demo

---

## 认证服务

### POST /auth/login

**接口说明**  
用户登录，获取访问令牌。

**请求体（Request Body）**

Content-Type: `application/json`

| 字段 | 类型   | 必填 | 说明   |
| ---- | ------ | ---- | ------ |
| username | string | 是   | 用户名 |
| password | string | 是   | 密码   |

**响应（Responses）**

- `200 OK`  
  Content-Type: `application/json`

  | 字段 | 类型   | 必填 | 说明       |
  | ---- | ------ | ---- | ---------- |
  | code | integer | 是   | 状态码     |
  | msg  | string  | 是   | 提示信息   |
  | data | object  | 是   | 返回数据   |
  | data.token | string | 是 | 访问令牌   |
  | data.userId | string | 是 | 用户 ID    |

- `400 Bad Request`  
  用户名或密码为空

- `401 Unauthorized`  
  用户名或密码错误

**示例**

请求：
```json
{
  "username": "admin",
  "password": "admin123"
}
```

响应：
```json
{
  "code": 200,
  "msg": "success",
  "data": {
    "token": "e32bb0d2-6cb0-453e-bb9a-b27f07e4c689",
    "userId": "1"
  }
}
```

---

## 用户服务

### GET /api/v1/user

**接口说明**  
获取当前登录用户信息。

**认证要求**  
需要在请求头中携带 `Authorization: Bearer <token>`

**响应（Responses）**

- `200 OK`  
  Content-Type: `application/json`

  | 字段 | 类型   | 必填 | 说明       |
  | ---- | ------ | ---- | ---------- |
  | code | integer | 是   | 状态码     |
  | msg  | string  | 是   | 提示信息   |
  | data | object  | 是   | 返回数据   |
  | data.userId | string | 是 | 用户 ID    |
  | data.username | string | 是 | 用户名     |
  | data.email | string | 是 | 邮箱       |

- `401 Unauthorized`  
  未授权或 token 无效

---

### GET /api/v1/users

**接口说明**  
获取用户列表。

**认证要求**  
需要在请求头中携带 `Authorization: Bearer <token>`

**响应（Responses）**

- `200 OK`  
  Content-Type: `application/json`

  | 字段 | 类型   | 必填 | 说明       |
  | ---- | ------ | ---- | ---------- |
  | code | integer | 是   | 状态码     |
  | msg  | string  | 是   | 提示信息   |
  | data | object  | 是   | 返回数据   |
  | data.list | array | 是 | 用户列表   |
  | data.total | integer | 是 | 总条数     |

**用户列表项结构**

| 字段 | 类型   | 必填 | 说明       |
| ---- | ------ | ---- | ---------- |
| id | string | 是   | 用户 ID    |
| username | string | 是 | 用户名     |
| email | string | 是 | 邮箱       |

---

### POST /api/v1/users

**接口说明**  
创建新用户。

**认证要求**  
需要在请求头中携带 `Authorization: Bearer <token>`

**请求体（Request Body）**

Content-Type: `application/json`

| 字段 | 类型   | 必填 | 说明   |
| ---- | ------ | ---- | ------ |
| username | string | 是   | 用户名 |
| password | string | 是   | 密码   |
| email | string | 否   | 邮箱   |

**响应（Responses）**

- `200 OK`  
  Content-Type: `application/json`

  | 字段 | 类型   | 必填 | 说明       |
  | ---- | ------ | ---- | ---------- |
  | code | integer | 是   | 状态码     |
  | msg  | string  | 是   | 提示信息   |
  | data | object  | 是   | 返回数据   |
  | data.id | string | 是 | 用户 ID    |
  | data.username | string | 是 | 用户名     |
  | data.email | string | 是 | 邮箱       |

- `400 Bad Request`  
  username/password 必填，或用户名已存在

---

### GET /api/v1/users/{user_id}

**接口说明**  
获取指定用户详情。

**认证要求**  
需要在请求头中携带 `Authorization: Bearer <token>`

**路径参数**

| 名称 | 类型   | 必填 | 说明     |
| ---- | ------ | ---- | -------- |
| user_id | string | 是   | 用户 ID  |

**响应（Responses）**

- `200 OK`  
  Content-Type: `application/json`

  | 字段 | 类型   | 必填 | 说明       |
  | ---- | ------ | ---- | ---------- |
  | code | integer | 是   | 状态码     |
  | msg  | string  | 是   | 提示信息   |
  | data | object  | 是   | 返回数据   |
  | data.id | string | 是 | 用户 ID    |
  | data.username | string | 是 | 用户名     |
  | data.email | string | 是 | 邮箱       |

- `404 Not Found`  
  用户不存在

---

### PUT /api/v1/users/{user_id}

**接口说明**  
更新指定用户信息。

**认证要求**  
需要在请求头中携带 `Authorization: Bearer <token>`

**路径参数**

| 名称 | 类型   | 必填 | 说明     |
| ---- | ------ | ---- | -------- |
| user_id | string | 是   | 用户 ID  |

**请求体（Request Body）**

Content-Type: `application/json`

| 字段 | 类型   | 必填 | 说明   |
| ---- | ------ | ---- | ------ |
| email | string | 否   | 邮箱   |
| password | string | 否   | 密码   |

**响应（Responses）**

- `200 OK`  
  Content-Type: `application/json`

  | 字段 | 类型   | 必填 | 说明       |
  | ---- | ------ | ---- | ---------- |
  | code | integer | 是   | 状态码     |
  | msg  | string  | 是   | 提示信息   |
  | data | object  | 是   | 返回数据   |
  | data.id | string | 是 | 用户 ID    |
  | data.username | string | 是 | 用户名     |
  | data.email | string | 是 | 邮箱       |

- `404 Not Found`  
  用户不存在

---

### DELETE /api/v1/users/{user_id}

**接口说明**  
删除指定用户。

**认证要求**  
需要在请求头中携带 `Authorization: Bearer <token>`

**路径参数**

| 名称 | 类型   | 必填 | 说明     |
| ---- | ------ | ---- | -------- |
| user_id | string | 是   | 用户 ID  |

**响应（Responses）**

- `200 OK`  
  Content-Type: `application/json`

  | 字段 | 类型   | 必填 | 说明       |
  | ---- | ------ | ---- | ---------- |
  | code | integer | 是   | 状态码     |
  | msg  | string  | 是   | 提示信息   |
  | data | null   | 是   | 返回数据   |

- `404 Not Found`  
  用户不存在

---

## 预置测试用户

| 用户名 | 密码 | 邮箱 |
|--------|------|------|
| admin | admin123 | admin@demo.com |
| test | test123 | test@demo.com |

## 服务配置

- 默认端口：`11011`
- 可通过环境变量 `DEMO_PORT` 自定义端口
- 数据存储：内存存储（重启后数据重置）
