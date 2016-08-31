var path = require("path"),
    webpack = require("webpack"),
    ExtractTextPlugin = require("extract-text-webpack-plugin"),
    ManifestRevisionPlugin = require("manifest-revision-webpack-plugin"),
    CleanWebpackPlugin = require('clean-webpack-plugin');

var root = "./assets";

module.exports = {
    entry: {
        app_js: [
            root + "/scripts/app.js"
        ],
        app_css: [
            root + "/styles/style.less"
        ]
    },
    output: {
        path: "./feature_request/build/public",
        publicPath: "http://localhost:2992/assets/",
        filename: "[name].[chunkhash].js",
        chunkFilename: "[id].[chunkhash].chunk"
    },
    resolve: {
        extensions: ["", ".js", ".less"]
    },
    module: {
        loaders: [
            {
                test: /\.js$/i,
                exclude: /(node_modules|assets\/styles)/,
                loader: "babel",
                query: {
                    cacheDirectory: true
                }
            },
            {
                test: /\.less$/i,
                exclude: /node_modules/,
                loader: ExtractTextPlugin.extract(['css!less'])
            }
        ]
    },
    plugins: [
        new webpack.NoErrorsPlugin(),
        new CleanWebpackPlugin(['public'], {
            root: process.cwd() + '/feature_request/build'
        }),
        new ExtractTextPlugin("[name].[chunkhash].css"),
        new ManifestRevisionPlugin(path.join("feature_request", "build", "manifest.json"), {
            rootAssetPath: root,
            ignorePaths: ["/styles", "/scripts"]
        }),
        new webpack.optimize.UglifyJsPlugin(),
        new webpack.optimize.DedupePlugin(),
        new webpack.DefinePlugin({
            "process.env": {
                NODE_ENV: '"production"'
            }
        })
    ]
};