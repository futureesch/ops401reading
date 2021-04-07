Reading02

https://aws.amazon.com/blogs/architecture/compute-abstractions-on-aws-a-visual-story/ 

Shared Responsibility Model between Cloud Service Providers and Consumers. 

“The higher you go in the abstraction levels, the more the cloud provider can add value and can offload the consumer from non-strategic activities.”

The instance (or virtual machine) abstraction - taking the physical server into abstraction with virtual machines as servers.

The container abstraction - “a container technology virtualizes an operating system so that you can run separated applications with different (and often incompatible) software dependencies.”

“With ECS and EKS, we have raised the abstraction level for the control plane, but we have not yet really raised the abstraction level for the data plane as the data plane is still comprised of regular EC2 instances that the customer has responsibility for.” However, “Fargate is making the containers data plane fall into the “Provider space” responsibility. This means the compute unit exposed to the user is the container abstraction, while AWS will manage transparently the data plane abstractions underneath.”

The function abstraction - AWS Lambda, or the abstracting away of everything

The bare metal abstraction - or “no abstraction,” for customers whose needs are not available virtually.

The full container abstraction (for lack of a better term)
