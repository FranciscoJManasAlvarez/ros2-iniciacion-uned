from geometry_msgs.msg import PoseStamped

from ros2_iniciacion_verificacion.verifier_base import (
    VerifierFailure,
    collect_messages,
    run_verifier,
    wait_for_node,
    wait_for_topic_type,
)


def check(node):
    wait_for_node(node, "nodo_goal_listener")
    wait_for_topic_type(node, "/robot1/objetivo", "geometry_msgs/msg/PoseStamped")

    pub = node.create_publisher(PoseStamped, "/goal_pose", 10)
    goal = PoseStamped()
    goal.header.frame_id = "map"
    goal.pose.position.x = 1.5
    goal.pose.position.y = -2.0

    import time

    time.sleep(0.5)
    pub.publish(goal)

    msgs = collect_messages(node, "/robot1/objetivo", PoseStamped, count=1, timeout=6.0)
    got = msgs[0]
    if abs(got.pose.position.x - 1.5) > 1e-3 or abs(got.pose.position.y - (-2.0)) > 1e-3:
        raise VerifierFailure("nodo_goal_listener no republica correctamente la pose recibida en /goal_pose")


def main():
    run_verifier("verificador_tema5_ej4", 4, check)


if __name__ == "__main__":
    main()
