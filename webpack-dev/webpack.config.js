var path = require('path');
var ExtractTextPlugin = require('extract-text-webpack-plugin');
var LiveReloadPlugin = require('webpack-livereload-plugin');


module.exports = {
    entry: "./entry.js",
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: "js/kirui.js"
    },
    module: {
        loaders: [
            {
                test: /\.scss$/,
                loader: ExtractTextPlugin.extract({
                    fallback: "style-loader",
                    use: [
                        {loader: "css-loader"},
                        {loader: "sass-loader"},
                    ]
                }),
            },
            {
                test: /\.woff2?$|\.ttf$|\.eot$|\.svg$/,
                use: [{
                    loader: "file-loader",
                    options: {
                        name: '[hash].[ext]',
                        useRelativePath: true
                    }
                }]
            }
        ]
    },
    plugins: [
        new ExtractTextPlugin("css/kirui.css"),
        new LiveReloadPlugin()
    ],
};