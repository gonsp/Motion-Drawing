#import "InputDetector.h"

@implementation InputDetector

// -----------------------------------
// Initialize the View
// -----------------------------------

- (id)initWithFrame:(NSRect)frame {
    self = [super initWithFrame:frame];
    [self setAllowedTouchTypes:YES];
    [self setWantsRestingTouches:YES];
    [self setWantsRestingTouches:YES];
    
    
    
    [NSEvent addGlobalMonitorForEventsMatchingMask:NSEventMaskMouseMoved handler:^(NSEvent * mouseEvent) {
        CGPoint pos = [mouseEvent locationInWindow];
        [self refresh:pos];
    }];
    
    return self;
}

- (void)refresh:(CGPoint)pos {
    int x = pos.x;
    int y = pos.y;
    
    [self send:CGPointMake(x, y)];
}

- (void)send:(CGPoint)pos {
    int x = pos.x;
    NSLog(@"%@", NSStringFromPoint(pos));
}

- (void)pressureChangeWithEvent:(NSEvent *)event {
    //NSLog(@"Pressure changed");
}

- (void)rotateWithEvent:(NSEvent *)event {
    NSLog(@"HELLOOOO");
}

- (void)scrollWheel:(NSEvent *)theEvent {
    //NSLog(@"user scrolled %f horizontally and %f vertically", [theEvent deltaX], [theEvent deltaY]);
}

@end



