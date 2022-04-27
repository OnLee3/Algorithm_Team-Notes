const Queue = function () {
  this.storage = {};
  this.front = 0;
  this.rear = 0;
};

Queue.prototype = {
  size() {
    if (this.storage[this.rear] === undefined) {
      return 0;
    } else {
      return this.rear - this.front + 1;
    }
  },
  push(value) {
    if (this.size() === 0) this.storage["0"] = value;
    else {
      this.rear++;
      this.storage[this.rear] = value;
    }
  },
  pop() {
    let value;
    if (this.front === this.rear) {
      value = this.storage[this.rear];
      delete this.storage[this.rear];
      this.front = 0;
      this.rear = 0;
    } else {
      value = this.storage[this.rear];
      delete this.storage[this.rear];
      this.rear--;
    }
    return value;
  },
  popleft() {
    let value;
    if (this.front === this.rear) {
      value = this.storage[this.front];
      delete this.storage[this.front];
      this.front = 0;
      this.rear = 0;
    } else {
      value = this.storage[this.front];
      delete this.storage[this.front];
      this.front++;
    }
    return value;
  },
};

export default Queue;
