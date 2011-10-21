var App = new Ext.Application({
    name: 'BeThereApp',
    useLoadmask: true,
    launch: function() {
        Ext.regModel('Bus', {
            fields: [
                { name: 'number', type: 'int'},
                { name: 'type', type: 'string'},
                { name: 'departure_time', type: 'date'},
                { name: 'direction', type: 'string'},
                { name: 'station_name', type: 'string'},
                { name: 'station_id', type: 'int'},
                { name: 'x', type: 'float'},
                { name: 'y', type: 'float'}
                ]
//           belongsTo: { model: 'BusList', name: 'bus_list' },
        });

//        Ext.regModel("BusList", {
//            fields: [
//                { name: '

        var testing_data = 
                [
                    {
                        number : '1',
                        type : 'Spårvagn',
                        departure_time : '2011-10-21 14:40',
                        direction : 'Test',
                        station_name : 'Test Station',
                        station_id : 12345,
                        x : 11.985889,
                        y : 57.70777
                    },    
                    {
                        number : '6',
                        type : 'Spårvagn',
                        departure_time : '2011-10-21 14:47',
                        direction : 'Test2',
                        station_name : 'Test Station',
                        station_id : 12345,
                        x : 11.985889,
                        y : 57.70777
                    }    
                ];

        Ext.regStore('busListStore', {
            autoLoad: true,
            model: 'Bus',
//            proxy: {
//                type: 'memory',
//                //type: 'ajax',
//                //method: 'get',
//                //url: '/get_buses',
//                //extraParams: {},
//                reader: {
//                    type: 'json',
//                    root: 'buses'
//                }
//            },
            //TODO:remove the testing data
            data: testing_data
        });

        
        var current_time = new Date();
        var one_minute = 1000*60;

        BeThereApp.views.busList = new Ext.List({
            id: 'busList',
            store: 'busListStore',
            itemTpl: new Ext.XTemplate(
                '<div class="list-item-name">{type} {number} at {station_name} in {[this.timeRemaining(values.departure_time)]}','&nbsp;mins.</div>','<div class="list-item-rarrative">Direction:{direction}</div>',
                { timeRemaining:function(departure_time) {return (Math.ceil((departure_time.getTime()-current_time.getTime())/one_minute)); }}
                ),
            onItemDisclosure: function (record) {
            //TODO:do something
            }
        });

        BeThereApp.views.busListToolbar = new Ext.Toolbar({
            id: 'busListToolbar',
            title: 'Bus List',
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

        BeThereApp.views.busListContainer = new Ext.Panel({
            id: 'busListContainer',
            layout: 'fit',
            html: 'This is the bus list container',
            dockedItems: [BeThereApp.views.busListToolbar],
            items: [BeThereApp.views.busList]
        });

        BeThereApp.views.viewport = new Ext.Panel({
            fullscreen: true,
            layout: 'card',
            cardAnimation: 'slide',
            items: [BeThereApp.views.busListContainer]
        });
    }
})
