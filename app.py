from App import create_app  # 从App包中导入create_app函数

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=5180)