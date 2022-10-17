from entities import QueryState


class HandlerManager():
    def __init__(self, sp, put_disp, extract_disp, load_disp):
        self.load_disp = load_disp
        self.extract_disp = extract_disp
        self.put_disp = put_disp
        self.sp = sp

    def process_new_event(self, query):
        self.put_disp.refused_query = None
        if query.state == QueryState.FROM_SOURCE:
            self.sp.handle(query)
        elif query.state == QueryState.FROM_INSTRUMENT:
            self.load_disp.instruments[query.n_instr].release()
            print("RELEASE INSTRUMENT HANDLER")
            self.extract_disp.handle()