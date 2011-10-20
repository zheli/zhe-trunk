var App = new Ext.Application({
    name: 'BeThereApp',
    useLoadmask: true,
    launch: function() {
        Ext.regModel('StationList', {
            fields: ['id', 'x', 'y', 'name'],
        });

        Ext.regStore('stationListStore', {
            model: 'StationList',
            proxy: {
            type: 'localstorage',
            id: 'bethere-app-localstore'
            },
            //TODO:remove the testing data
            data: [
                {id: 7459105, x: 11.980877, y: 57.70769, name:'Barnhusgatan'},
                {id: 7459478, x: 11.980877, y: 57.70769, name:'Polhemsplatsen'}
            ]
        });

        BeThereApp.views.stationList = new Ext.List({
            id: 'stationList',
            store: 'stationListStore',
            itemTpl: '<div class="list-item-name">{name}</div>',
            onItemDisclosure: function (record) {
            //TODO:do something
            }
        });

        BeThereApp.views.stopListToolbar = new Ext.Toolbar({
            id: 'stopListToolbar',
            title: 'Stations Around Me',
            layout: 'hbox',
            items: [
                { xtype: 'spacer' },
                {
                    id: 'locateButton',
                    text: 'Locate',
                    ui: 'action',
                    handler: function() {
                    //TODO: do something here
                    }
                }
            ]
        });

        BeThereApp.views.stopListContainer = new Ext.Panel({
            id: 'stopListContainer',
            layout: 'fit',
            html: 'This is the stop list container',
            dockedItems: [BeThereApp.views.stopListToolbar],
            items: [BeThereApp.views.stationList]
        });

        BeThereApp.views.viewport = new Ext.Panel({
            fullscreen: true,
            layout: 'card',
            cardAnimation: 'slide',
            items: [BeThereApp.views.stopListContainer]
        });
    }
})
