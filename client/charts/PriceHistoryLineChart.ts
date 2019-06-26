import Component from 'vue-class-component';
import {Mixins, Prop} from 'vue-property-decorator';
import {Line} from 'vue-chartjs';

@Component({
    extends: Line,
})
export default class PriceHistoryLineChart extends Mixins(Line) {
    @Prop()
    public data!: any;

    async mounted() {
        this.renderChart(this.data, {
            responsive: true,
            maintainAspectRatio: false,
            legend: {
                display: false,
            },
            scales: {
                xAxes: [{
                    display: false,
                    gridLines: {
                        display: false,
                        drawBorder: false,
                    },
                }],
                yAxes: [{
                    gridLines: {
                        display: false,
                        drawBorder: false,
                    },
                }],
            },
            elements: {
                line: {
                    fill: false,
                },
            },
        });
    }
}
