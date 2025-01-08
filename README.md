# 戴佳伟 老年人活动 录播汇总

- http://djw.line.pm/
- https://www.gzher.com/djwcb/

## 构建流程

### Github Pages
```
# 在本地构建 将项目克隆到本地 并在本地配置好 Vue 环境（记得 npm install）

python build.py # 生成 Vue 代码

(vue-project) npm run build # 构建 Vue 项目

# 将变动推送到 Github
```

### VPS
```
# 在 VPS 构建 将项目克隆到服务器 并在服务器上配置好 Vue 环境（记得 npm install）

# 将配置文件 "vue-project/vue.config.js" 删除 改为使用 "vue-project/vue.config.js.vps"

(vue-project) npm run build # 构建 Vue 项目
```
