% Run: ILASP 03_ilasp.las
% ILASP-specific learning task: body predicates allowed only positively.
#modeh(can_enter(var(robot))).
#modeb(charged(var(robot)), (positive)).
#modeb(door_open(var(robot)), (positive)).
#maxv(1).

% Positive: must derive can_enter(r1) in this context.
#pos({can_enter(r1)}, {}, {
    robot(r1).
    charged(r1).
    door_open(r1).
}).

% Negative: must not derive can_enter(r2), charged but closed door.
#neg({can_enter(r2)}, {}, {
    robot(r2).
    charged(r2).
}).

% Negative: must not derive can_enter(r3), open door but uncharged.
#neg({can_enter(r3)}, {}, {
    robot(r3).
    door_open(r3).
}).
