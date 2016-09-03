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
        ],
        vendor_js: [
            './node_modules/angular/angular.js'
        ]
    },
    output: {
        path: "./feature_request/build/public",
        publicPath: "http://localhost:2992/assets/",
        filename: "[name].js",
        chunkFilename: "[id].chunk"
    },
    resolve: {
        extensions: ["", ".js", ".less"]
    },
    module: {
        preLoaders: [
            {
                test: /\.js$/,
                exclude: [
                    /node_modules/,
                    /\.spec\.js$/
                ],
                loader: 'isparta-loader'
            }
        ],
        loaders: [

            {
                test: /\.js$/i,
                exclude: /(node_modules|assets\/styles)/,
                loader: "ng-annotate!babel"
            },
            {
                test: /\.less$/i,
                exclude: /node_modules/,
                loader: ExtractTextPlugin.extract('css!less')
            },
            {
                test: /\.html$/,
                loader: 'ngtemplate?relativeTo=' + (path.resolve(__dirname, './assets/scripts')) + '/!html'
            }
        ]
    },
    plugins: [
        new webpack.NoErrorsPlugin(),
        new ExtractTextPlugin("[name].css"),
        new ManifestRevisionPlugin(path.join("feature_request", "build", "manifest.json"), {
            rootAssetPath: root,
            ignorePaths: ["/styles", "/scripts"]
        }),
        new webpack.optimize.DedupePlugin(),
        new webpack.DefinePlugin({
            "process.env": {
                NODE_ENV: '"production"'
            }
        })
    ],
    devtool: "inline-source-map"
};