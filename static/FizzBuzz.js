'use strict';

const { Component } = React;
const { render } = ReactDOM;

class FizzBuzz extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: []
    };
  }

  componentDidMount() {
    fetch('/fizzbuzz')
      .then(response => response.json())
      .then(data => this.setState({ data }));
  }

  render() {
    const { data } = this.state;

    const listItems = data.map((item, index) => {
      return React.createElement('li', { key: index }, item);
    });

    const ul = React.createElement('ul', null, listItems);
    const div = React.createElement('div', { className: 'FizzBuzz' }, ul);

    return div;
  }
}

render(React.createElement(FizzBuzz), document.getElementById('root'));