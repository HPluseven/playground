class EventBus {
  constructor() {
    if (!EventBus.instance) {
      this.eventQueues = {};
      EventBus.instance = this;
    }
    return EventBus.instance;
  }

  on(eventName, callback) {
    if (!this.eventQueues[eventName]) {
      this.eventQueues[eventName] = [callback];
    } else {
      this.eventQueues.push(callback);
    }
  }

  emit(eventName, payload) {
    if (!this.eventQueues[eventName]) {
      console.log("No eventName");
      return;
    }
    this.eventQueues[eventName].forEach((callback) => {
      callback(payload);
    });
  }

  off(eventName, callback) {
    const idx = callback ? this.eventQueues[eventName].indexOf(callback) : -1;

    if (idx > 0 && this.eventQueues[eventName].length > 1) {
      this.eventQueues[eventName].splice(idx, 1);
      console.log("delete ", idx);
    } else {
      delete this.eventQueues[eventName];
      console.log("delete all");
    }
  }

  once(eventName, callback) {
    let once = (payload) => {
      this.off(eventName, callback);
      callback(payload);
    };
    this.on(eventName, once);
  }
}

const eventBus = new EventBus();
const eventBus2 = new EventBus();
console.log(eventBus === eventBus2);
const callback = (payload) => {
  console.log(payload);
};
eventBus.once("test", callback);
// eventBus.on("test", callback);
eventBus.on("test2", (payload) => {
  console.log(payload);
});

eventBus.emit("test", { name: "xiaoming" });
// eventBus.off("test", callback);
eventBus.emit("test", { name: "xiaoming" });
