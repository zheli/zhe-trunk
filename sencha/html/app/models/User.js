App.models.User = Ext.regModel('Item', {
    fields: [
        {
            name: 'item_title',
            type: 'string',
        }, {
            name: 'item_price',
            type: 'float',
        }, {
            name: 'lat',
            type: 'float',
        }, {
            name: 'lon',
            type: 'float',
        }, {
            name: 'currency',
            type: 'int',
        }, {
            name: 'image_url',
            type: 'string'
        }, {
            name: 'thumbnail_url',
            type: 'string'
        }
    ],

    validations: [
        {
            type: 'presence',
            name: 'item_title'
        }
    ],

    proxy: {
        type: 'localstorage',
        id: 'sencha-users'
    }
});
