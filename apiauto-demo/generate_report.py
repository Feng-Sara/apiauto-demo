import json
import os

def main():
    results_dir = 'f:/MyProjects/apiauto-demo/allure-results'

    passed = 0
    failed = 0
    cases = []

    for filename in os.listdir(results_dir):
        if filename.endswith('-result.json'):
            with open(os.path.join(results_dir, filename), 'r', encoding='utf-8') as f:
                data = json.load(f)
                status = data.get('status', 'unknown')
                params = data.get('parameters', [])
                case_info = {}
                for p in params:
                    if p.get('name') == 'row':
                        try:
                            row_data = eval(p.get('value', '{}'))
                            case_info = row_data
                        except:
                            pass
                
                case = {
                    'id': case_info.get('用例ID', data.get('name', '')),
                    'name': case_info.get('用例名称', data.get('name', '')),
                    'method': case_info.get('请求方法', ''),
                    'path': case_info.get('接口路径', ''),
                    'status': status,
                    'expected_status': case_info.get('预期状态码', ''),
                    'priority': case_info.get('优先级', '')
                }
                cases.append(case)
                if status == 'passed':
                    passed += 1
                else:
                    failed += 1

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>API 测试报告</title>
    <style>
        body {{ font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif; margin: 20px; background: #f5f5f5; }}
        .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 30px; border-radius: 12px; margin-bottom: 20px; }}
        .header h1 {{ margin: 0; font-size: 28px; }}
        .summary {{ display: flex; gap: 20px; margin-bottom: 20px; }}
        .stat {{ background: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); flex: 1; text-align: center; }}
        .stat h3 {{ margin: 0; font-size: 14px; color: #666; }}
        .stat p {{ margin: 10px 0 0; font-size: 36px; font-weight: bold; }}
        .passed {{ color: #28a745; }}
        .failed {{ color: #dc3545; }}
        .total {{ color: #17a2b8; }}
        .percent {{ color: #666; font-size: 16px !important; }}
        table {{ width: 100%; border-collapse: collapse; background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
        th, td {{ padding: 12px; text-align: left; border-bottom: 1px solid #eee; }}
        th {{ background: #f8f9fa; font-weight: 600; color: #495057; }}
        tr:hover {{ background: #f8f9fa; }}
        .status-pass {{ background: #d4edda; color: #155724; padding: 4px 10px; border-radius: 20px; font-size: 12px; font-weight: 600; }}
        .status-fail {{ background: #f8d7da; color: #721c24; padding: 4px 10px; border-radius: 20px; font-size: 12px; font-weight: 600; }}
        .priority-p0 {{ color: #dc3545; font-weight: bold; }}
        .priority-p1 {{ color: #fd7e14; }}
        .method {{ padding: 4px 10px; border-radius: 4px; font-size: 12px; font-weight: 600; }}
        .method-get {{ background: #17a2b8; color: white; }}
        .method-post {{ background: #28a745; color: white; }}
        .method-put {{ background: #fd7e14; color: white; }}
        .method-delete {{ background: #dc3545; color: white; }}
        .footer {{ margin-top: 20px; text-align: center; color: #666; font-size: 14px; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>API 自动化测试报告</h1>
        <p style="margin: 10px 0 0; opacity: 0.9;">测试时间: 2026-05-15</p>
    </div>
    
    <div class="summary">
        <div class="stat">
            <h3>总用例数</h3>
            <p class="total">{passed + failed}</p>
        </div>
        <div class="stat">
            <h3>通过</h3>
            <p class="passed">{passed}</p>
        </div>
        <div class="stat">
            <h3>失败</h3>
            <p class="failed">{failed}</p>
        </div>
        <div class="stat">
            <h3>通过率</h3>
            <p class="percent">{((passed / (passed + failed)) * 100):.1f}%</p>
        </div>
    </div>

    <table>
        <thead>
            <tr>
                <th>用例ID</th>
                <th>用例名称</th>
                <th>请求方法</th>
                <th>接口路径</th>
                <th>预期状态码</th>
                <th>优先级</th>
                <th>状态</th>
            </tr>
        </thead>
        <tbody>'''

    for case in sorted(cases, key=lambda x: x['id']):
        method_class = 'method-' + case['method'].lower() if case['method'] else ''
        status_class = 'status-pass' if case['status'] == 'passed' else 'status-fail'
        priority_class = 'priority-' + case['priority'].lower() if case['priority'] else ''
        
        html += f'''
            <tr>
                <td>{case['id']}</td>
                <td>{case['name']}</td>
                <td><span class="method {method_class}">{case['method']}</span></td>
                <td>{case['path']}</td>
                <td>{case['expected_status']}</td>
                <td><span class="{priority_class}">{case['priority']}</span></td>
                <td><span class="{status_class}">{case['status']}</span></td>
            </tr>'''

    html += '''
        </tbody>
    </table>
    
    <div class="footer">
        <p>API 测试报告 - 由 Trae AI 生成</p>
    </div>
</body>
</html>'''

    with open('f:/MyProjects/apiauto-demo/test-report.html', 'w', encoding='utf-8') as f:
        f.write(html)

    print('报告已生成: f:/MyProjects/apiauto-demo/test-report.html')

if __name__ == '__main__':
    main()
