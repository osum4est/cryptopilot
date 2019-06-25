const path = require("path");

module.exports = {
  devServer: {
    proxy: {
      '/api*': {
        target: 'http://localhost:8000/'
      }
    }
  },
  chainWebpack: config => {
    config
      .entry("app")
      .clear()
      .add("./client/main.ts")
      .end();
    config.resolve.alias
      .set("@", path.join(__dirname, "./client"))
  },
};
