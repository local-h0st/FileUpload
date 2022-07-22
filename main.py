from flask import Flask, request, render_template, redirect, flash, get_flashed_messages
import os

mainApp = Flask(__name__)
mainApp.secret_key = 'localh0st'


@mainApp.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        if not file:
            flash('empty file')
            return redirect('/')
        # file.save(os.path.join('uploads', file.filename))     可以
        # file.save('uploads/',file.filename)   这种是错的，但是为什么错的原因是permission denied?
        flash("上传成功,path : /uploads/" + file.filename)  # 也可以
        return redirect('/')
    else:
        return render_template('upload.html', msg=get_flashed_messages())


# 但是直接访问是访问不到的，因为没定义路由


if __name__ == '__main__':
    mainApp.run(debug=True)
