#!/usr/bin/env python3
"""
启动本地HTTP服务器来展示架构发现页面
"""

import http.server
import socketserver
import os
import sys
import webbrowser
from pathlib import Path

def start_server(port=8000):
    """启动HTTP服务器"""
    
    # 获取当前脚本所在目录
    current_dir = Path(__file__).parent.absolute()
    
    # 切换到当前目录
    os.chdir(current_dir)
    
    # 创建HTTP服务器
    Handler = http.server.SimpleHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", port), Handler) as httpd:
            print(f"🚀 服务器启动成功!")
            print(f"📁 服务目录: {current_dir}")
            print(f"🌐 访问地址: http://localhost:{port}")
            print(f"📄 主页面: http://localhost:{port}/index.html")
            print("\n" + "="*50)
            print("💡 使用说明:")
            print("1. 点击 '开始发现之旅' 开始展示")
            print("2. 点击 '自动播放' 连续展示所有架构")
            print("3. 新发现的架构会自动高亮显示")
            print("4. 第37个架构会触发特殊里程碑")
            print("="*50)
            print("\n按 Ctrl+C 停止服务器")
            
            # 自动打开浏览器
            try:
                webbrowser.open(f'http://localhost:{port}/index.html')
                print("🌐 已自动打开浏览器...")
            except:
                print("⚠️  无法自动打开浏览器，请手动访问上述地址")
            
            # 启动服务器
            httpd.serve_forever()
            
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ 端口 {port} 已被占用，尝试使用端口 {port + 1}")
            start_server(port + 1)
        else:
            print(f"❌ 启动服务器失败: {e}")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n👋 服务器已停止")
        sys.exit(0)

if __name__ == "__main__":
    print("🎯 AI Architecture Discovery Server")
    print("正在启动本地服务器...")
    start_server() 