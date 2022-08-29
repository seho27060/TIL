package com.ssafy.specificPJ.Repository;

import com.ssafy.specificPJ.Domain.Member;
import org.springframework.data.jpa.repository.JpaRepository;

public interface MemberRepository extends JpaRepository<Member,Long> {
    Member findById(int id);
}
