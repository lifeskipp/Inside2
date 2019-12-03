var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
(function (factory) {
    if (typeof module === "object" && typeof module.exports === "object") {
        var v = factory(require, exports);
        if (v !== undefined) module.exports = v;
    }
    else if (typeof define === "function" && define.amd) {
        define(["require", "exports", "../../../common/view.abstract"], factory);
    }
})(function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    const view_abstract_1 = __importDefault(require("../../../common/view.abstract"));
    class ErrorView extends view_abstract_1.default {
        constructor(code) {
            super("status");
            this.params["title"] = "Ooops... Something went wrong!";
            this.params["message"] = `You got error ${code}, it means that ${ErrorCodes[+code]}.`;
        }
    }
    exports.default = ErrorView;
    const ErrorCodes = {
        404: "file not found",
        403: "access forbidden"
    };
});
//# sourceMappingURL=index.js.map