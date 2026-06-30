# Touchless Provisioning Workflow

This document explains the end-to-end private cloud automation flow represented by this repository.

## Phase 0 — Infrastructure

VMware Cloud Foundation provides the integrated platform foundation. SDDC Manager coordinates lifecycle operations for the management stack, including vCenter, NSX, and vSAN.

## Phase 1 — Network

NSX provides isolated tenant networking. In a production implementation, this may include VPC constructs, segments, gateways, distributed firewall policies, and north-south routing boundaries.

## Phase 2 — IPAM and DNS

Aria Automation Extensibility triggers ABX actions that reserve an address from phpIPAM and create DNS records. The DNS example uses RFC 2136 dynamic updates against BIND9.

## Phase 3 — Load balancing

NSX Advanced Load Balancer can publish application endpoints using Service Engines placed in the correct network context. This repo only includes placeholders for that phase today.

## Phase 4 — Kubernetes

Aria Automation requests a VKS workload cluster. The Supervisor handles the lifecycle of the workload cluster after the request is submitted through the platform service.

## Phase 5 — Security

A vSphere Namespace is created, quota limits are assigned, and Kubernetes RBAC bindings are mapped to identity groups.

## Phase 6 — Operations

The workflow can update CMDB or ticketing systems and send operational notifications to Microsoft Teams.

## Phase 7 — Developer handoff

The requester receives the information required to access the cluster and begin deploying workloads.
