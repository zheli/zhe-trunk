Ext.ns('bethere', 'bethere.views');

Ext.setup({
    statusBarStyle: 'black',
    onReady: function() {
        bethere.app = new bethere.app({
            title: 'BeThere'
        });
    }
});
