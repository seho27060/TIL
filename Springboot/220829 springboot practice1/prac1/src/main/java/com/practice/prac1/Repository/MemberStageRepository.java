package com.practice.prac1.Repository;

import com.practice.prac1.Domain.MemberStage;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface MemberStageRepository extends JpaRepository<MemberStage, Long> {
    Optional<MemberStage> findByMember_idAndStage_id(Long member, Long stage);
    Optional<MemberStage> findByMember_id(Long member);
}
