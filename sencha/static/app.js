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
        ],
//           belongsTo: { model: 'BusList', name: 'bus_list' },
           proxy: {type: 'localstorage', id: 'buslistproxy'}
});
var busListStore = new Ext.data.Store({
    model: 'Bus',
    autoload: true,
    proxy: {
        type: 'ajax',
        method: 'get',
        url: '/get_buses',
        extraParams: {},
        reader: {
            type: 'json'
        }
    }
});

var current_time = new Date();
var one_minute = 1000*60;

bethere.views.busListContainer = Ext.extend(Ext.Panel, {
    layout: 'fit',
    html: 'this is the bus list container',
    initComponent: function() {
        this.list = new Ext.List({
            cls: 'timeline',
            emptyText: 'Cannot retrieve data',
            disableSelection: true,
            store: busListStore,
            itemCls: 'busitem',
            itemTpl: Ext.XTemplate(
                '<div class="list-item-name">{type} {number} at {station_name} in {[this.timeRemaining(values.departure_time)]}','&nbsp;mins.</div>','<div class="list-item-rarrative">Direction:{direction}</div>',
                { timeRemaining:function(departure_time) {return (Math.ceil((departure_time.getTime()-current_time.getTime())/one_minute)); }}
            ),
            listeners: {
                //itemtap: function (list, index, element, event) {
                    //TODO: do some real things here
                //}
            }
        });

        this.list.on('render', function(){
            this.list.store.load();
            this.list.el.mask('<span class="top"></span><span class="right"></span><span class="left"></span>', 'x-spinner', false);
        }, this);

        busListToolbar = new Ext.Toolbar({
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
        this.dockedItems = busListToolbar;
        bethere.views.busListContainer.superclass.initComponent.call(this);
    }
});

Ext.reg('buslistcontainer', bethere.views.busListContainer);

bethere.app = Ext.extend(Ext.Panel, {
    fullscreen: true,
    layout: 'card',
    cardAnimation: 'slide',
    initComponent: function() {
        this.items = [bethere.views.busListContainer];
        bethere.app.superclass.initComponent.call(this);
    }
});
