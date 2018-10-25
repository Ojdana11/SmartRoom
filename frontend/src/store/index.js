import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        count: 0,
        cards: [{
                card: {
                    title: 'I am one card1',
                    description: 'xDDD'
                },
                'card-type': 'card1'
            },
            {
                card: {
                    title: 'I am one card2',
                    description: 'xDDD2'
                },
                'card-type': 'card1'
            }
        ],
        devices: {}
    },

    mutations: {
        increment(state) {
            state.count++;
        },
        addCard(state, payload) {
            state.cards.push(payload.card);
        },
        devices(state, payload) {
            state.devices = payload.devices;
        }
    }
})